## ShortIO
ShortIO library is intended to avoid context manager boilerplate in simple io operations. The library supports plain text, JSON, pickle and YAML (PyYAML impl).

Inspired by [ilio](https://github.com/gowhari/ilio).

### Installation
```bash
pip install shortio
```

### Usage

#### Plain text read & write:
```python
from shortio import read, write

s = read('filename')
write('filename', s)
```

#### Binary data read & write:
```python
from shortio import read, write

s = read('filename', 'rb')
write('filename', s, 'wb')
```

#### JSON data read & write:
```python
from shortio import read_json, write_json

d = read_json('filename.json')
write_json('filename.json', d)
```

#### Pickle data read & write:
```python
from shortio import read_pickle, write_pickle

d = read_pickle('filename.pkl')
write_pickle('filename.pkl', d)
```

#### YAML data read & write:

Since python does not support YAML out of the box you have to install PyYAML.

```bash
pip install PyYAML>=5.1
```

```python
from shortio import read_yaml, write_yaml

d = read_yaml('filename.yaml')
write_yaml('filename.yaml', d)
```
