import pytest
import uuid
import json
import random
import string
import requests
from class_test import SEL
from lead_creator import LeadsCreator
from courier_sender import CourierSender
from courier_services import Couriers


@pytest.fixture
def port(request):
    return request.config.getoption('--port')

@pytest.fixture
def time_out(request):
    return request.config.getoption('--time')

@pytest.fixture
def pparam(request):
    return request.config.getoption('--pparam')

@pytest.fixture
def host(request):
    return request.config.getoption('--host')

@pytest.fixture
def port_web_api(request):
    return request.config.getoption('--web-api')

@pytest.fixture
def host(request):
    return request.config.getoption('--host')

@pytest.fixture
def lead_creat(host,port_web_api):
    oid = LeadsCreator().cr_lead(host=host,port=port_web_api)
    return oid

@pytest.fixture
def test_auth(host,port):
    SEL().auth(host=host,port=port)


@pytest.mark.parametrize("courier, partner", Couriers.couriers)
def test_change_lead_status_and_send_courier(test_auth,time_out,pparam,host,port_web_api, lead_creat,courier,partner):
    oid = lead_creat
    SEL().orders(time_out=time_out)
    SEL().find_identifer(time_out=time_out,oid=oid)
    SEL().order_change_status(time_out=time_out,pparam=pparam)
    LeadsCreator().check_status_of_lead(oid=oid)
    CourierSender().courier(time_out=time_out)
    CourierSender().courier_lead(time_out=time_out, oid=lead_creat)
    CourierSender().send_to_courier(time_out=time_out)
    CourierSender().choose_courier_services(time_out=time_out, courier=courier, partner=partner)
    SEL().compare_data(time_out=time_out, courier=courier, partner=partner)
    SEL().driver.delete_all_cookies()


def test_close_driver():
    SEL().close_driver()




