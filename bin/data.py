from enum import Enum
from dataclasses import dataclass, asdict, fields
import dataclasses
from itertools import chain
import json
from pathlib import Path
from typing import List, Any, Dict, Type

# Tomli was subsumed into Python 3.11.x, but was renamed to to tomllib.
# This avoids ci failures for Python < 3.11.2.
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib



def _custom_dataclass_init(self, *args, **kwargs):
    # print(self.__class__.__name__, "__init__")
    names = [field.name for field in fields(self)]
    used_names = set()

    # Handle positional arguments
    for value in args:
        try:
            name = names.pop(0)
        except IndexError:
            raise TypeError(f"__init__() given too many positional arguments")
        # print(f'setting {k}={v}')
        setattr(self, name, value)
        used_names.add(name)

    # Handle keyword arguments
    for name, value in kwargs.items():
        if name in names:
            # print(f'setting {k}={v}')
            setattr(self, name, value)
            used_names.add(name)
        elif name in used_names:
            raise TypeError(f"__init__() got multiple values for argument '{name}'")
        else:
            raise TypeError(
                f"Unrecognized field '{name}' for dataclass {self.__class__.__name__}."
                "\nIf this field is valid, please add it to the dataclass in data.py."
                "\nIf adding an object-type field, please create a new dataclass for it."
            )

    # Check for missing positional arguments
    missing = [
        f"'{field.name}'" for field in fields(self)
        if isinstance(field.default, dataclasses._MISSING_TYPE) and field.name not in used_names
    ]
    if len(missing) == 1:
        raise TypeError(f"__init__() missing 1 required positional argument: {missing[0]}")
    elif len(missing) == 2:
        raise TypeError(f"__init__() missing 2 required positional arguments: {' and '.join(missing)}")
    elif len(missing) != 0:
        missing[-1] = f"and {missing[-1]}"
        raise TypeError(f"__init__() missing {len(missing)} required positional arguments: {', '.join(missing)}")

    # Run post init if available
    if hasattr(self, "__post_init__"):
        self.__post_init__()


@dataclass
class TrackStatus:
    __init__ = _custom_dataclass_init

    concept_exercises: bool = False
    test_runner: bool = False
    representer: bool = False
    analyzer: bool = False


class IndentStyle(str, Enum):
    Space = "space"
    Tab = "tab"


@dataclass
class TestRunnerSettings:
    average_run_time: float = -1


@dataclass
class EditorSettings:
    __init__ = _custom_dataclass_init

    indent_style: IndentStyle = IndentStyle.Space
    indent_size: int = 4
    ace_editor_language: str = "python"
    highlightjs_language: str = "python"

    def __post_init__(self):
        if isinstance(self.indent_style, str):
            self.indent_style = IndentStyle(self.indent_style)


class ExerciseStatus(str, Enum):
    Active = "active"
    WIP = "wip"
    Beta = "beta"
    Deprecated = "deprecated"


@dataclass
class ExerciseFiles:
    __init__ = _custom_dataclass_init

    solution: List[str]
    test: List[str]
    editor: List[str] = None
    exemplar: List[str] = None


    # practice exercises are different
    example: List[str] = None

    def __post_init__(self):
        if self.exemplar is None:
            if self.example is None:
                raise ValueError(
                    "exercise config must have either files.exemplar or files.example"
                )
            else:
                self.exemplar = self.example
                delattr(self, "example")
        elif self.example is not None:
            raise ValueError(
                "exercise config must have either files.exemplar or files.example, but not both"
            )


@dataclass
class ExerciseConfig:
    __init__ = _custom_dataclass_init

    files: ExerciseFiles
    authors: List[str] = None
    forked_from: str = None
    contributors: List[str] = None
    language_versions: List[str] = None
    test_runner: bool = True
    source: str = None
    source_url: str = None
    blurb: str = None
    icon: str = None

    def __post_init__(self):
        if isinstance(self.files, dict):
            self.files = ExerciseFiles(**self.files)
        for attr in ["authors", "contributors", "language_versions"]:
            if getattr(self, attr) is None:
                setattr(self, attr, [])

    @classmethod
    def load(cls, config_file: Path) -> "ExerciseConfig":
        with config_file.open() as f:
            return cls(**json.load(f))


@dataclass
class ExerciseInfo:
    __init__ = _custom_dataclass_init

    path: Path
    slug: str
    name: str
    uuid: str
    prerequisites: List[str]
    type: str = "practice"
    status: ExerciseStatus = ExerciseStatus.Active

    # concept only
    concepts: List[str] = None

    # practice only
    difficulty: int = 1
    topics: List[str] = None
    practices: List[str] = None

    def __post_init__(self):
        if self.concepts is None:
            self.concepts = []
        if self.topics is None:
            self.topics = []
        if self.practices is None:
            self.practices = []
        if isinstance(self.status, str):
            self.status = ExerciseStatus(self.status)

    @property
    def solution_stub(self):
        return next(
            (
                p
                for p in self.path.glob("*.py")
                if not p.name.endswith("_test.py") and p.name != "example.py"
            ),
            None,
        )

    @property
    def helper_file(self):
        return next(self.path.glob("*_data.py"), None)

    @property
    def test_file(self):
        return next(self.path.glob("*_test.py"), None)

    @property
    def meta_dir(self):
        return self.path / ".meta"

    @property
    def exemplar_file(self):
        if self.type == "concept":
            return self.meta_dir / "exemplar.py"
        return self.meta_dir / "example.py"

    @property
    def template_path(self):
        return self.meta_dir / "template.j2"

    @property
    def config_file(self):
        return self.meta_dir / "config.json"

    def load_config(self) -> ExerciseConfig:
        return ExerciseConfig.load(self.config_file)


@dataclass
class Exercises:
    __init__ = _custom_dataclass_init

    concept: List[ExerciseInfo]
    practice: List[ExerciseInfo]
    foregone: List[str] = None

    def __post_init__(self):
        if self.foregone is None:
            self.foregone = []
        for attr_name in ["concept", "practice"]:
            base_path = Path("exercises") / attr_name
            setattr(
                self,
                attr_name,
                [
                    (
                        ExerciseInfo(path=(base_path / e["slug"]), type=attr_name, **e)
                        if isinstance(e, dict)
                        else e
                    )
                    for e in getattr(self, attr_name)
                ],
            )

    def all(self, status_filter={ExerciseStatus.Active, ExerciseStatus.Beta}):
        return [
            e for e in chain(self.concept, self.practice) if e.status in status_filter
        ]


@dataclass
class Concept:
    __init__ = _custom_dataclass_init

    uuid: str
    slug: str
    name: str


@dataclass
class Feature:
    __init__ = _custom_dataclass_init

    title: str
    content: str
    icon: str


@dataclass
class FilePatterns:
    __init__ = _custom_dataclass_init

    solution: List[str]
    test: List[str]
    example: List[str]
    exemplar: List[str]
    editor: List[str] = None



@dataclass
class Config:
    __init__ = _custom_dataclass_init

    language: str
    slug: str
    active: bool
    status: TrackStatus
    blurb: str
    version: int
    online_editor: EditorSettings
    exercises: Exercises
    concepts: List[Concept]
    key_features: List[Feature] = None
    tags: List[Any] = None
    test_runner: TestRunnerSettings = None
    files: FilePatterns = None

    def __post_init__(self):
        if isinstance(self.status, dict):
            self.status = TrackStatus(**self.status)
        if isinstance(self.online_editor, dict):
            self.online_editor = EditorSettings(**self.online_editor)
        if isinstance(self.test_runner, dict):
            self.test_runner = TestRunnerSettings(**self.test_runner)
        if isinstance(self.exercises, dict):
            self.exercises = Exercises(**self.exercises)
        if isinstance(self.files, dict):
            self.files = FilePatterns(**self.files)
        self.concepts = [
            (Concept(**c) if isinstance(c, dict) else c) for c in self.concepts
        ]
        if self.key_features is None:
            self.key_features = []
        if self.tags is None:
            self.tags = []

    @classmethod
    def load(cls, path="config.json"):
        try:
            with Path(path).open() as f:
                return cls(**json.load(f))
        except IOError:
            print(f"FAIL: {path} file not found")
            raise SystemExit(1)
        except TypeError as ex:
            print(f"FAIL: {ex}")
            raise SystemExit(1)


@dataclass
class TestCaseTOML:
    __init__ = _custom_dataclass_init

    uuid: str
    description: str
    include: bool = True
    comment: str = ''


@dataclass
class TestsTOML:
    __init__ = _custom_dataclass_init

    cases: Dict[str, TestCaseTOML]

    @classmethod
    def load(cls, toml_path: Path):
        with toml_path.open("rb") as f:
            data = tomllib.load(f)
        return cls({uuid: TestCaseTOML(uuid, *opts) for
                    uuid, opts in
                    data.items() if
                    opts.get('include', None) is not False})


if __name__ == "__main__":

    class CustomEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Path):
                return str(obj)
            return json.JSONEncoder.default(self, obj)

    config = Config.load()
    print(json.dumps(asdict(config), cls=CustomEncoder, indent=2))
