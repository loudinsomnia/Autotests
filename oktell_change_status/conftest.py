import pytest


def pytest_addoption(parser):
    parser.addoption("--host",action="store",default='',help='specify host of test')
    parser.addoption("--port",action="store",default='',help='specify host of test')

