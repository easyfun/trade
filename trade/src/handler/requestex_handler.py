#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2016年12月20日

@author: ASPRCK
'''
import tornado.web
import json


class RequestExHandler(tornado.web.RequestHandler):
#     def __init__(self,application, request, **kwargs):
#         super(RequestExHandler,self).__init__(application, *request, **kwargs)
#         self.response={
#             'err_code':0,
#             'err_msg':''
#         }

    def initialize(self):
        self.now_time=None
        self.body_from_json = None
        self.response={
            'err_code':0,
            'err_msg':''
        }

    
    def load_body(self):
        self.body_from_json = json.loads(self.request.body)

    
    def check_function_call(self, func, *args, **kwargs):
        if not func(*args, **kwargs):
            self.write(json.dumps(self.response))
            return False
        return True


    def set_response(self,err_code, err_msg, data=None):
        self.response['err_code']=err_code
        self.response['err_msg']=err_msg
        if None != data:
            self.response['data']=data
        
    
    def set_response_error(self, error):
        self.set_response(error[0], error[1])
    
    
    def write_response(self):
        self.write(json.dumps(self.response))
    

    
