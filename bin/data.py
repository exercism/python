from enum import Enum
from dataclasses import dataclass, asdict
import json
from pathlib import Path
from typing import List, Any


@dataclass
class TrackStatus:
    concept_exercises: bool = False
    test_runner: bool = False
    representer: bool = False
    analyzer: bool = False


class IndentStyle(str, Enum):
    Space = 'space'
    Tab = 'tab'


@dataclass
class EditorSettings:
    indent_style: IndentStyle = IndentStyle.Space
    indent_size: int = 4

    def __post_init__(self):
        if isinstance(self.indent_style, str):
            self.indent_style = IndentStyle(self.indent_style)


class ExerciseStatus(str, Enum):
    Active = 'active'
    WIP = 'wip'
    Beta = 'beta'
    Deprecated = 'deprecated'


@dataclass
class ExerciseInfo:
    path: Path
    slug: str
    name: str
    uuid: str
    prerequisites: List[str]
    type: str = 'practice'
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
        return next((
            p for p in self.path.glob('*.py')
            if not p.name.endswith('_test.py') and
            p.name != 'example.py'
        ), None)

    @property
    def test_file(self):
        return next(self.path.glob('*_test.py'), None)

    @property
    def meta_dir(self):
        return self.path / '.meta'

    @property
    def exemplar_file(self):
        if self.type == 'concept':
            return self.meta_dir / 'exemplar.py'
        return self.meta_dir / 'example.py'

    @property
    def template_path(self):
        return self.meta_dir / 'template.j2'

    @property
    def config_file(self):
        return self.meta_dir / 'config.json'


@dataclass
class Exercises:
    concept: List[ExerciseInfo]
    practice: List[ExerciseInfo]
    foregone: List[str] = None

    def __post_init__(self):
        if self.foregone is None:
            self.foregone = []
        for attr_name in ['concept', 'practice']:
            base_path = Path('exercises') / attr_name
            setattr(
                self,
                attr_name,
                [
                    (
                        ExerciseInfo(
                            path=(base_path / e['slug']),
                            type=attr_name,
                            **e
                        ) if isinstance(e, dict) else e
                    )
                    for e in getattr(self, attr_name)
                ]
            )

    def all(self, include_deprecated=False):
        _all = self.concept + self.practice
        if not include_deprecated:
            _all = [e for e in _all if e.status != ExerciseStatus.Deprecated]
        return _all


@dataclass
class Concept:
    uuid: str
    slug: str
    name: str
    blurb: str


@dataclass
class Feature:
    title: str
    content: str
    icon: str


@dataclass
class Config:
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

    def __post_init__(self):
        if isinstance(self.status, dict):
            self.status = TrackStatus(**self.status)
        if isinstance(self.online_editor, dict):
            self.online_editor = EditorSettings(**self.online_editor)
        if isinstance(self.exercises, dict):
            self.exercises = Exercises(**self.exercises)
        self.concepts = [
            (Concept(**c) if isinstance(c, dict) else c)
            for c in self.concepts
        ]
        if self.key_features is None:
            self.key_features = []
        if self.tags is None:
            self.tags = []

    @classmethod
    def load(cls, path='config.json'):
        try:
            with Path(path).open() as f:
                return cls(**json.load(f))
        except IOError:
            print(f'FAIL: {path} file not found')
            raise SystemExit(1)


if __name__ == "__main__":
    class CustomEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Path):
                return str(obj)
            return json.JSONEncoder.default(self, obj)

    config = Config.load()
    print(json.dumps(asdict(config), cls=CustomEncoder, indent=2))
