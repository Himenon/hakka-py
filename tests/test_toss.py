"""Tests for `hakka` package."""

import pytest

from click.testing import CliRunner

import sys

sys.path.append('/src')

from hakka import hakka
from hakka import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'hakka.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_same_callback():
    app = hakka.Hakka()

    _test_key = 'test:func'

    @app.watch(_test_key)
    def test_func():
        pass

    params = app._config.get(_test_key)
    callback = params.get('callback')

    assert test_func == callback
