#!/usr/bin/env python
# -*- coding:utf-8 -*-


from tornado.test.util import unittest
import tornado.httpclient

class UserRegisterTest(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_user_register(self):
        client=tornado.httpclient.HTTPClient()


if '__main__'==__name__:
    pass