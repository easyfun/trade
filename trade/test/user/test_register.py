#!/usr/bin/env python
# -*- coding:utf-8 -*-


from tornado.test.util import unittest
import tornado.httpclient
import json

class UserRegisterTest(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_user_register(self):
        client=tornado.httpclient.HTTPClient()
        body={'mobile':'1351729a5502'}
        encode_body=json.dumps(body)
        request=tornado.httpclient.HTTPRequest(
            r'http://127.0.0.1:8080/user/register',
            method='POST',
            body=encode_body
            )
        response=client.fetch(request)
#         print(response)
        print(response.body)


if '__main__'==__name__:
    unittest.main()