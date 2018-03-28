import pytest
from hakka import Hakka


@pytest.fixture
def app():
    return Hakka()
