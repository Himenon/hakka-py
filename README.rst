====
toss
====


.. image:: https://img.shields.io/pypi/v/toss.svg
        :target: https://pypi.python.org/pypi/toss

.. image:: https://img.shields.io/travis/himenon/toss.svg
        :target: https://travis-ci.org/himenon/toss

.. image:: https://readthedocs.org/projects/toss/badge/?version=latest
        :target: https://toss.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/himenon/toss/shield.svg
     :target: https://pyup.io/repos/github/himenon/toss/
     :alt: Updates



Small Task Queue


* Free software: MIT license
* Documentation: https://toss.readthedocs.io.


Usage
-----

*Receiver*

.. code-block:: python

    from toss import Toss

    app = Toss()

    @app.watch('hello:msg', redis_dtype='list', redis_vtype='json')
    def hello_msg(name=None, msg=None, **kwargs):
        print("Hello {name}!, {msg}".format(name=name, msg=msg))

    app.listen('localhost', 6379, 0, debug=True)


*Sender*

.. code-block:: shell

    redis-cli lpush hello:msg '{"name": "yourname", "msg": "Congratulation!"}'


Features
--------

* TODO

- Cluster


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
