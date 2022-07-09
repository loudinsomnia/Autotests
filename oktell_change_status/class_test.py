import time

import pyodbc as odbs
import requests
import json
import uuid
import random
import string
import pytest
from params_list import ParamList
from oidscreator import OidCreator


class RequestOid:
    def request(self,params,host,port):
        if port == '':
            url_status_change = f'http://{host}'
        else:
            url_status_change = f'http://{host}:{port}'
        re = requests.request("GET", url=url_status_change, headers=OidCreator.headers, params=params)
        return re

    def valid_change_status(self,host,port):
        params = ParamList().params(host=host,port=port)['valid_params']
        re = self.request(params=params,host=host,port=port)
        assert re.status_code == 200, f"Error status code {re.status_code} on valid data"
        print(time.perf_counter())

    def wrong_oid(self,host,port):
        params = ParamList().params(host=host,port=port)['wrong_oid']
        re = self.request(params=params,host=host,port=port)
        assert re.status_code == 400, f"Wrong status code {re.status_code} on wrong oid data"
        print(time.perf_counter())

    def nonexecute_statuses(self,host,port):
        params = ParamList().params(host=host,port=port)['nonexecute_statuses']
        re = self.request(params=params,host=host,port=port)
        assert re.status_code == 400, f"Wrong status code {re.status_code} on nonexist status"
        print(time.perf_counter())

    def with_out_substatus_for_Rejected(self,port,host):
        params = ParamList().params(host=host,port=port)['with_out_substatus_for_Rejected']
        re = self.request(params=params,host=host,port=port)
        assert re.status_code == 200, f"Wrong status code {re.status_code} for status with out substatus"
        print(time.perf_counter())

    def with_out_substatus_for_Declined(self,host,port):
        params = ParamList().params(host=host,port=port)['with_out_substatus_for_Declined']
        re = self.request(params=params,host=host,port=port)
        assert re.status_code == 200, f"Wrong status code {re.status_code} for status with out substatus"
        print(time.perf_counter())

    def process_without_delivery(self,host,port):
        params = ParamList().params(host=host,port=port)['process_without_delivery']
        re = self.request(params=params,host=host,port=port)
        assert re.status_code == 400, f"Wrong status code {re.status_code} for status with out delivery"
        print(time.perf_counter())

