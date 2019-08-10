from .builtins_wrapper import read, write
from .builtins_wrapper import read_json, write_json
from .builtins_wrapper import read_pickle, write_pickle

try:
    from .yaml_wrapper import read_yaml, write_yaml
except ImportError:
    pass

# TODO Add feature to use kwargs for specific formats.

from .__version__ import __version__
