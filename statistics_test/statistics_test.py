import time
import pytest
from test_class import SEL
from xpath import Xpath
from xpath_for_newview_pages import Xpath_newwiev
from xpath_for_statistics_with_required import Xpath_for_required


@pytest.fixture
def port(request):
    return request.config.getoption('--port')


@pytest.fixture
def host(request):
    return request.config.getoption('--host')


@pytest.fixture
def time_out(request):
    return request.config.getoption('--time')


@pytest.mark.dependency()
def test_auth(port, host):
    SEL().auth(port=port, host=host)
    print(time.perf_counter())


@pytest.mark.dependency(depends=["test_auth"])
@pytest.mark.parametrize("page, xpath", Xpath_newwiev.xpath)
def test_new_view_statistics(time_out, page, xpath):
    SEL().new_view_statistics(time_out=time_out, xpath=xpath)
    print(time.perf_counter())


@pytest.mark.dependency(depends=["test_auth"])
@pytest.mark.parametrize('page, xpath, required, for_place, selector', Xpath_for_required.xpath_required_webmasters)
def test_webmasters_analitics(time_out, page, xpath, required, for_place, selector):
    SEL().statistics_with_required_fields(time_out=time_out, xpath=xpath, required=required, for_place=for_place,
                                          selector=selector)
    print(time.perf_counter())


@pytest.mark.dependency(depends=["test_auth"])
@pytest.mark.parametrize("page, xpath, selector, table_param", Xpath_for_required.xpath_required_warehous)
def test_warehous_statistics(time_out, page, xpath, selector, table_param):
    SEL().warehous_statistics(time_out=time_out, xpath=xpath, selector=selector, table_param=table_param)
    print(time.perf_counter())


@pytest.mark.dependency(depends=["test_auth"])
@pytest.mark.parametrize('page, xpath, selector', Xpath.xpath)
def test_statistics(time_out, xpath, selector, page):
    SEL().statistics_page(xpath=xpath, time_out=time_out)
    SEL().statistic_execute(time_out=time_out, selector=selector)
    print(time.perf_counter())


def test_close_driver():
    SEL.driver.delete_all_cookies()
    SEL.driver.quit()
    print(time.perf_counter())
