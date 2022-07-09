import pytest

def pytest_addoption(parser):
    parser.addoption("--port", action="store", default='', help="specify port of test host")
    parser.addoption("--web-api",action="store",default='',help="specify port of test host")
    parser.addoption("--time",action="store",default='5000', help="time wait for CRM pages")
    parser.addoption("--pparam", action="store",default=False,help="Product parametr is exist")
    parser.addoption("--host", action="store", default='', help="host")


