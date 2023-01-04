from contextlib import contextmanager
from enum import Enum
from pathlib import Path
import shutil
import subprocess
from contextlib import suppress
from typing import Iterator, Union


GITHUB_EXERCISM = "https://github.com/exercism"


class Repo(Enum):
    ProblemSpecifications = f"{GITHUB_EXERCISM}/problem-specifications.git"


def clone(repo: Union[str, Repo], directory: Union[str, Path, None] = None) -> bool:
    if isinstance(repo, Repo):
        repo = repo.value
    if directory is None:
        directory = repo.split("/")[-1].split(".")[0]
    directory = Path(directory)
    if not directory.is_dir():
        with suppress(subprocess.CalledProcessError):
            subprocess.run(["git", "clone", repo, str(directory)], check=True)
            return True
    return False


@contextmanager
def clone_if_missing(repo: Union[str, Repo], directory: Union[str, Path, None] = None) -> Iterator[None]:
    temp_clone = clone(repo, directory)
    try:
        yield directory
    finally:
        if temp_clone:
            shutil.rmtree(directory)
