from hakka import Hakka
from unittest import TestCase
from mock import MagicMock


def test_initial_params(app):
    assert app.conn is None
    assert app.debug is False
    assert app.max_retry_count == 60
    assert app.retry_connection_interval == 5
    assert app.beat_interval == 0.01
    assert app.timeout == 30
    assert app.watch_keys == []


def test_watch(app):
    # mock_func = MagicMock()
    # mock_func.__name__ = 'mock_func'
    @app.watch("hello")
    def my_func():
        return "HELLO"

    print(my_func)
    assert my_func() == "HELLO"


def tearDown(self):
    pass
