import yaml
from typing import Any

from .utils import PathType


def read_yaml(file: PathType) -> Any:
    with open(file, 'r') as f:
        # TODO Add feature to use different loaders.
        return yaml.full_load(f)


def write_yaml(file: PathType, obj: Any) -> None:
    with open(file, 'w') as f:
        yaml.dump(obj, f)
