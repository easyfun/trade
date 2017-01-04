#!/usr/bin/env python
# -*- coding:utf-8 -*-


from tornado.test.util import unittest
import tornado.httpclient
import json

import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

class UserRegisterTest(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_user_register(self):
        client=tornado.httpclient.HTTPClient()
        body={'mobile':'13517295502','user_type':2L,'login_password':'123456'}
        encode_body=json.dumps(body)
        request=tornado.httpclient.HTTPRequest(
            r'http://127.0.0.1:8080/user/register',
            method='POST',
            body=encode_body
            )
        response=client.fetch(request)
#         print(response)
        print(json.dumps(response.body))
#         print(response.body.get('err_msg'))
        rj=json.loads(response.body)
#         print(rj)
        print(rj['err_msg'])
        print(rj['err_code'])

if '__main__'==__name__:
    unittest.main()