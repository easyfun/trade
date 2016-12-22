#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2016年12月19日

@author: ASPRCK
'''


import utils.tool
from handler.requestex_handler import RequestExHandler
from dao.user_dao import UserDao 
from model.user import UserType, FromType
from model.user import User
from exception.error_code import UserErrorCode
import tornado.httpclient
import tornado.gen
import json
from exception import error_code

class RegisterHandler(RequestExHandler):
#     def get(self):
#         self.write('ok')

    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        self.load_body()
        #print(self.body_from_json)
        
        if not self.check_function_call(self.check_request):
            self.finish()
            return        
        
        user=User()
        user.mobile=self.body_from_json.get('mobile')
        user.user_type=self.body_from_json.get('user_type')
        user.from_type=self.body_from_json.get('from_type', FromType.UNKNOWN)
        user.login_password=self.body_from_json.get('login_password')
#         print(user)
        
        http_client=tornado.httpclient.AsyncHTTPClient()
        user_id_resp=yield tornado.web.gen.Task(http_client.fetch,
                    'http://127.0.0.1:8080/id/user_id?suffix=%s' % (
                    user.mobile[-2:],))
        user_id_body=json.loads(user_id_resp.body)
#         print(user_id_body)
        if error_code.SUCCESS_CODE != user_id_body['err_code']:
            self.set_response_error(UserErrorCode.CREATE_USER_ID_ERROR)
            self.finish()
            return
        user.user_id=user_id_body['data']
#         print(user)
        
        self.write_response()
        self.finish()
        

    def check_request(self):
        #检查手机号
        if 0==len(self.body_from_json['mobile']):
            self.set_response_error(UserErrorCode.ARGUMENT_MOBILE_ERROR)
            return False

        if not utils.tool.is_numerical_string(self.body_from_json['mobile']):
            self.set_response_error(UserErrorCode.ARGUMENT_MOBILE_ERROR)
            return False
        
        #手机号是否已注册
        user_dao=UserDao()
        user=user_dao.get_user_by_mobile(self.body_from_json['mobile'])
        if user != None:
            self.set_response(UserErrorCode.MOBILE_HAS_EXSITED)
            return False
        
        #检查登录密码
        if len(self.body_from_json['login_password']) < 6:
            self.set_response_error(UserErrorCode.ARGUMENT_PASSWORD_ERROR)
            return False
        
        #检查用户类型
        if not UserType.is_valid(self.body_from_json['user_type']):
            self.set_response_error(UserErrorCode.ARGUMENT_USE_TYPE_ERROR)
            return False
        
        
        return True

        
        
        
        
        
        
        
        
        
        
        