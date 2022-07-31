import pytest as pytest

from base.base_request import BaseRequest
from utils.logger.logger import Logger

date_time_regex = r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}.?[0-9]+Z?"
phone_regex = r"[0-9]{10}"
url_regex = "http://www.[a-z]*.com"
coords_regex = r"[-]{0,1}[0-9]{2}.[0-9]{7}"
postal_regex = r"^[0-9]{5}(?:-[0-9]{4})?$"
list_cities = ["san_diego", "miami"]
list_types = ["micro", "nano", "regional", "brewpub", "large", "planning", "bar", "contract", "proprietor", "closed"]


@pytest.fixture(scope="session", autouse=True)
def initial_setup():
    Logger.create_logger()
    yield


@pytest.fixture()
def request_brewerie(request):
    if hasattr(request.cls, "params"):
        params = request.cls.params
    else:
        params = ""
    if hasattr(request.cls, "command"):
        command = request.cls.command
    else:
        command = ""
    return BaseRequest.get(command, params=params)


@pytest.fixture(scope="class", params=list_cities)
def get_city(request):
    return request.param


@pytest.fixture(scope="class", params=list_types)
def get_type(request):
    return request.param

