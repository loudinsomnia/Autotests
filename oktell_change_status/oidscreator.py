import pyodbc as odbs
import requests
import json
import uuid
import random
import string
import pytest

class OidCreator:
    headers = {'x-api-key': '',
               'Content-Type': 'application/json'}
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


    def create_lead(self,host,port):
        if port == '':
            url = f'http://{host}'
        else:
            url = f'http://{host}:{port}'
        product = '16173000'
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
            "WebmasterId": "веб1",
            "LeadFee": 0
        })
        re = requests.request("POST", url=url, headers=self.headers, data=js)
        assert re.status_code == 200, f"Error status {re.status_code}"
        return re.text


    def bd_connection(self,host,port):
        lead_id = self.create_lead(host=host,port=port)
        self.cursor.execute(f"SELECT TOP (1000) [Oid] FROM [LeadsCRM].[dbo].[Lead] WHERE [Id] = {lead_id}")
        oid = self.cursor.fetchone()
        for i in oid:
            return i


    def randomize_oid(self):
        generate_oid = ''.join(random.choice(string.digits + string.ascii_uppercase) for _ in range(8)) + \
                       '-' + ''.join(random.choice(string.digits + string.ascii_uppercase) for _ in range(4)) + \
                       '-' + ''.join(random.choice(string.digits + string.ascii_uppercase) for _ in range(4)) + \
                       '-' + ''.join(random.choice(string.digits + string.ascii_uppercase) for _ in range(4)) + \
                       '-' + ''.join(random.choice(string.digits + string.ascii_uppercase) for _ in range(12))
        return generate_oid

    def close_bd(self):
        self.cursor.close()
        self.conn.close()
