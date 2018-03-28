"""Tests for `hakka` package."""

import pytest
from click.testing import CliRunner
from mock import Mock
from hakka import Hakka, cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_hakka_watch():
    h = Hakka()
    mymethod = Mock()
    mymethod.return_value = 'watch-test'


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'hakka.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_same_callback(app):
    _test_key = 'test:func'

    @app.watch(_test_key)
    def test_func():
        pass

    params = app._config.get(_test_key)
    callback = params.get('callback')

    assert test_func == callback
