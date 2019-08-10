import json
import pickle
from typing import Any, AnyStr

from .utils import PathType


def read(file: PathType, mode: str = 'r') -> AnyStr:
    with open(file, mode) as f:
        return f.read()


def write(file: PathType, s: AnyStr, mode: str = 'w') -> None:
    with open(file, mode) as f:
        f.write(s)


def read_json(file: PathType) -> Any:
    with open(file, 'r') as f:
        return json.load(f)


def write_json(file: PathType, obj: Any) -> None:
    with open(file, 'w') as f:
        json.dump(obj, f)


def read_pickle(file: PathType) -> Any:
    with open(file, 'rb') as f:
        return pickle.load(f)


def write_pickle(file: PathType, obj: Any) -> None:
    with open(file, 'wb') as f:
        pickle.dump(obj, f)
