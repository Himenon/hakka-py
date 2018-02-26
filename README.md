# hakka

[![PyPi Status](https://img.shields.io/pypi/v/hakka.svg)](https://pypi.org/project/hakka/)
[![Travis CI Status](https://img.shields.io/travis/himenon/hakka.svg)](https://travis-ci.org/himenon/hakka)
[![Documentation Status](https://readthedocs.org/projects/hakka/badge/?version=latest)](https://hakka.readthedocs.io/en/latest/?badge=latest)
[![Updates](https://pyup.io/repos/github/himenon/hakka/shield.svg)](https://pyup.io/repos/github/himenon/hakka-py/)

Small Task Queue

* Free software: MIT license
* Documentation: <https://hakka.readthedocs.io>.

## Usage

```bash
$ pip install hakka
```

**Receiver**

```python
from hakka import Hakka

app = Hakka()

@app.watch('hello:msg', redis_dtype='list', redis_vtype='json')
def hello_msg(name=None, msg=None, **kwargs):
    print("Hello {name}!, {msg}".format(name=name, msg=msg))

app.listen('localhost', 6379, 0, debug=True)
```

**Sender**

```bash
$ redis-cli lpush hello:msg '{"name": "yourname", "msg": "Congratulation!"}'
```

## How to Develop

Using: Docker, docker-compose

```bash
$ docker-compose up
# start pytest-watch
```

## Relase

```bash
$ docker-compose run dev bash
$ make dist
$ make release
```

## Features

* TODO
    - クラスター対応
    - エラー対応
    - CIの追加

