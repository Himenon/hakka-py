====
hakka
====


.. image:: https://img.shields.io/pypi/v/hakka.svg
        :target: https://pypi.python.org/pypi/hakka

.. image:: https://img.shields.io/travis/himenon/hakka.svg
        :target: https://travis-ci.org/himenon/hakka

.. image:: https://readthedocs.org/projects/hakka/badge/?version=latest
        :target: https://hakka.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/himenon/hakka/shield.svg
     :target: https://pyup.io/repos/github/himenon/hakka/
     :alt: Updates



Small Task Queue


* Free software: MIT license
* Documentation: https://hakka.readthedocs.io.


Usage
-----

*Receiver*

.. code-block:: python

    from hakka import Hakka

    app = Hakka()

    @app.watch('hello:msg', redis_dtype='list', redis_vtype='json')
    def hello_msg(name=None, msg=None, **kwargs):
        print("Hello {name}!, {msg}".format(name=name, msg=msg))

    app.listen('localhost', 6379, 0, debug=True)


*Sender*

.. code-block:: shell

    redis-cli lpush hello:msg '{"name": "yourname", "msg": "Congratulation!"}'


How to Develop
--------------

Using: Docker, docker-compose

.. code-block:: shell

    docker-compose up
    # start pytest-watch


Features
--------

* TODO
    - クラスター対応
    - エラー対応
    - CIの追加

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
