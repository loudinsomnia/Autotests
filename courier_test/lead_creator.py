import pytest
import requests
import pyodbc as odbs
import random
import uuid
import json
import string

class LeadsCreator:
    DRIVER_NAME = 'SQL Server'
    SERVER_NAME = 'server'
    DATABASE = 'database'
    user_name = 'login'
    passwd = 'pass'

    connection_string = f"Driver={DRIVER_NAME};" \
                        f"Server={SERVER_NAME};" \
                        f"Database={DATABASE};" \
                        f"uid={user_name};" \
                        f"pwd={passwd}"
    conn = odbs.connect(connection_string)
    cursor = conn.cursor()


    def cr_lead(self,host,port):
        if port == '':
            url = f'http://{host}'
        else:
            url = f'http://{host}:{port}'
        headers = {'x-api-key': 'api-key',
                   'Content-Type': 'application/json'}
        product = '31550'
        md5 = uuid.uuid4().hex
        js = json.dumps({
            "ExternalCode": "qa" + md5,
            "Name": "watch SAM",
            "Phone": '904' + ''.join(random.choice(string.digits) for i in range(7)),
            "LandingSplit": "BG_Factor30",
            "Products": [
                {
                    "ProductId": product,
                    "Quantity": 0
                }
            ],
            "WebmasterId": "10006",
            "LeadFee": 0
        })
        re = requests.request("POST", url=url, headers=headers, data=js)
        assert re.status_code == 200, f"Error {re.status_code}{re.text}"
        return re.text

    def check_status_of_lead(self,oid):
        self.cursor.execute(f"SELECT TOP (1000) [Status],[Substatus] FROM [LeadsCRM].[dbo].[Lead] WHERE [Id] = {oid}")
        status = self.cursor.fetchone()
        assert status[0] == 15,f"Status not saved"
        assert status[1] == 128, f"SubStatus not saved"