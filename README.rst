============
hakka-py
============

.. image:: https://img.shields.io/pypi/v/hakka.svg
        :target: https://pypi.python.org/pypi/hakka

.. image:: https://img.shields.io/travis/Himenon/hakka-py.svg
        :target: https://travis-ci.org/Himenon/hakka-py

.. image:: https://readthedocs.org/projects/hakka-py/badge/?version=latest
        :target: https://hakka-py.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/Himenon/hakka-py/shield.svg
     :target: https://pyup.io/repos/github/Himenon/hakka-py/
     :alt: Updates


Small Task Queue

* Free software: MIT license
* Documentation: <https://hakka.readthedocs.io>.

Usage
=====

.. code-block::bash

    $ pip install hakka


**Receiver**

.. code-block::python

    from hakka import Hakka

    app = Hakka()

    @app.watch('hello:msg', redis_dtype='list', redis_vtype='json')
    def hello_msg(name=None, msg=None, **kwargs):
        print("Hello {name}!, {msg}".format(name=name, msg=msg))

    app.listen('localhost', 6379, 0, debug=True)

**Sender**

.. code-block::bash

    $ redis-cli lpush hello:msg '{"name": "yourname", "msg": "Congratulation!"}'

How to Develop
==============

Using: Docker, docker-compose

.. code-block::bash

    $ docker-compose up
    # start pytest-watch

