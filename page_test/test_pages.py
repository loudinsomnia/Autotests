import pytest
from class_test import SEL
from xpath import Xpath
import time

@pytest.fixture
def port(request):
    return request.config.getoption('--port')


@pytest.fixture
def time_out(request):
    return request.config.getoption('--time')

@pytest.fixture
def host(request):
    return request.config.getoption('--host')

@pytest.mark.dependency()
def test_auth(port,host):
    function = SEL()
    function.auth(port=port,host=host)
    print(time.perf_counter())


@pytest.mark.dependency(depends=["test_auth"])
@pytest.mark.parametrize("page, xpath",Xpath.xpath)
def test_pages(time_out,page,xpath):
    function = SEL()
    function.mass_function(time_out=time_out, xpath=xpath)
    print(time.perf_counter())


def test_close_driver():
    SEL.driver.delete_all_cookies()
    SEL.driver.quit()
    print(time.perf_counter())
