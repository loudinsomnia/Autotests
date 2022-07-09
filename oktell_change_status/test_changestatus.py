import pytest
from class_test import RequestOid
from oidscreator import OidCreator



@pytest.fixture
def host(request):
    return request.config.getoption('--host')
@pytest.fixture
def port(request):
    return request.config.getoption('--port')

def test_valid_change_status(host,port):
    RequestOid().valid_change_status(host=host,port=port)

def test_wrong_oid(host,port):
    RequestOid().wrong_oid(host=host,port=port)

def test_nonexecute_statuses(host,port):
    RequestOid().nonexecute_statuses(host=host,port=port)

def test_with_out_substatus_for_Rejected(host,port):
    RequestOid().with_out_substatus_for_Rejected(host=host,port=port)

def test_with_out_substatus_for_Declined(host,port):
    RequestOid().with_out_substatus_for_Declined(host=host,port=port)

def test_process_without_delivery(host,port):
    RequestOid().process_without_delivery(host=host,port=port)
    OidCreator().close_bd()