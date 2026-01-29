from email.policy import default


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action = "store",
        default = "dev",
        help = "environment name"
    )


import pytest

@pytest.fixture
def env(request):
    return request.config.getoption("--env")
