import pytest

def pytest_addoption(parser):
    parser.addini(
        "default_country",
        "Default country from pytest.ini",
        default="INDIA"
    )

    # command line
    parser.addoption(
        "--country",
        action="store",
        help="Country code from command line"
    )

@pytest.fixture
def country(request):
    cmd_country = request.config.getoption("--country")
    ini_country = request.config.getini("default_country")
    return cmd_country \
        if cmd_country else ini_country
