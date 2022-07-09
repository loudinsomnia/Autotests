import pytest
from oidscreator import OidCreator

class ParamList:
    crm_user_oid = '001f9c7b-c6dd-467a-9a7b-1c9d8955ca49'
    def params(self,host,port):
        params = {'valid_params': {'orderId': OidCreator().bd_connection(host,port),
                                   'statusCode': 2,
                                   'callId': OidCreator().randomize_oid(),
                                   'crmUserOid': self.crm_user_oid},
                  'wrong_oid': {'orderId': OidCreator().randomize_oid(),
                                'statusCode': 6,
                                'callId': OidCreator().randomize_oid(),
                                'crmUserOid': self.crm_user_oid},
                  'nonexecute_statuses': {'orderId': OidCreator().bd_connection(host,port),
                                          'statusCode': 15,
                                          'callId': OidCreator().randomize_oid(),
                                          'crmUserOid': self.crm_user_oid},
                  'with_out_substatus_for_Rejected': {'orderId': OidCreator().bd_connection(host,port),
                                                      'statusCode': 4,
                                                      'callId': OidCreator().randomize_oid(),
                                                      'crmUserOid': self.crm_user_oid},
                  'with_out_substatus_for_Declined': {'orderId': OidCreator().bd_connection(host,port),
                                                      'statusCode': 5,
                                                      'callId': OidCreator().randomize_oid(),
                                                      'crmUserOid': self.crm_user_oid},
                  'process_without_delivery': {'orderId': OidCreator().bd_connection(host,port),
                                               'statusCode': 3,
                                               'callId': OidCreator().randomize_oid(),
                                               'crmUserOid': self.crm_user_oid}
                  }
        return params