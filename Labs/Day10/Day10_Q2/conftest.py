import pytest

@pytest.fixture(scope="function")
def numbers():
    return (10, 5)

@pytest.fixture(scope="module")
def sample_text():
    return "pytest"
