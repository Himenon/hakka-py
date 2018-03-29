import pytest
import asyncio


def test_initial_params(app):
    assert app.debug is False
    assert app.max_retry_count == 60
    assert app.retry_connection_interval == 5
    assert app.beat_interval == 0.01
    assert app.timeout == 30
    assert app._watch_keys == []


def test_watch_keys(app):
    @app.watch("func-1")
    def func1():
        pass

    @app.watch("func-2")
    def func2():
        pass

    assert len(app.watch_keys) == 2
    assert "func-1" in app.watch_keys
    assert "func-2" in app.watch_keys


@pytest.mark.skip()
def test_listen(app):
    pass


def test_get_func(app):
    @app.watch("func1-key")
    def func1():
        return "my method"

    @app.watch("func2-key")
    def func2(name=None, age=None):
        return "{}, {}".format(name, age)

    assert func1 is app.get_func("func1-key")
    assert func2 is app.get_func("func2-key")


def test_logger(app):
    import logging
    assert app.logger.name == 'hakka.app'
    assert app.logger.level == logging.NOTSET


@pytest.mark.skip()
def test_watch(app):
    # mock_func = MagicMock()
    # mock_func.__name__ = 'mock_func'
    @app.watch("hello")
    def my_func():
        return "HELLO"

    assert my_func() == "HELLO"


# http://jacobbridges.github.io/post/unit-testing-with-asyncio/
@pytest.mark.skip(reason="一旦放置")
def test_run_task(app, client):
    will_change_value = None

    check_key = "change-mock-value"
    client.set_value(check_key, {})

    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)

    @app.watch(check_key)
    def change_value():
        global will_change_value
        will_change_value = 1

    async def run_test():
        app.run_task()
        assert will_change_value == 1

    coro = asyncio.coroutine(run_test)
    event_loop.run_until_complete(coro())
    event_loop.close()


def test_watch_tasks():
    pass
