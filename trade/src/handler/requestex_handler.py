#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2016年12月20日

@author: ASPRCK
'''
import tornado.web
import json
from datetime import datetime
from exception import error_code


class RequestExHandler(tornado.web.RequestHandler):
#     def __init__(self,application, request, **kwargs):
#         super(RequestExHandler,self).__init__(application, *request, **kwargs)
#         self.response={
#             'err_code':0,
#             'err_msg':''
#         }

    def initialize(self):
        self.mysql_client=None
        self.mysql_client_flow=None
        self.body=None
        self.now_time=datetime.date()
        self.response={
            'err_code':0,
            'err_msg':''
        }

    
    #弃用
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
    

    def finish_handler(self):
        self.write(json.dumps(self.response))
        self.finish()

    def finish_handler_commit(self):
        if not self.mysql_client:
            self.mysql_client.close_commit()
        
        if not self.mysql_client_flow:
            self.mysql_client_flow.close_commit()
        
        self.write(json.dumps(self.response))
        self.finish()


    def finish_handler_roll_back(self):
        if not self.mysql_client:
            self.mysql_client.close_roll_back()
        
        if not self.mysql_client_flow:
            self.mysql_client_flow.close_commit()

        self.write(json.dumps(self.response))
        self.finish()


    @classmethod
    def get_id(response):
        body=json.loads(response.body)
#         print(user_id_body)
        if error_code.SUCCESS_CODE != body.get('err_code',-1):
            return -1        
        data=body.get('data',-1)
        return data

    
