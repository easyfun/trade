#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2016年12月19日

@author: ASPRCK
'''


import utils.tool
from handler.requestex_handler import RequestExHandler
from dao.user_dao import UserDao 
from model.user import UserType, FromType, UserStatus
from model.user import User
from exception.error_code import UserErrorCode
import tornado.httpclient
import tornado.gen
import json
from exception import error_code
from datetime import datetime

class RegisterHandler(RequestExHandler):
#     def get(self):
#         self.write('ok')

    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        user=User()
        if not self.check_function_call(self.check_request, user):
            self.finish()
            return        
        
        http_client=tornado.httpclient.AsyncHTTPClient()
        user_id_resp=yield tornado.web.gen.Task(http_client.fetch,
                    'http://127.0.0.1:8080/id/user_id?suffix=%s' % (
                    user.mobile[-2:],))
        user_id_body=json.loads(user_id_resp.body)
#         print(user_id_body)
        if error_code.SUCCESS_CODE != user_id_body.get('err_code',-1):
            self.set_response_error(UserErrorCode.CREATE_USER_ID_ERROR)
            self.finish()
            return
        user.user_id=user_id_body.get('data',-1)
        if -1==user.user_id:
            self.set_response_error(UserErrorCode.CREATE_USER_ID_ERROR)
            self.finish()
            return
        
        user.update_time=datetime.date()
        user.create_time=user.update_time
        self.write_response()
        self.finish()
        

    def check_request(self,user):
        body = json.loads(self.request.body)
        user.mobile=body.get('mobile','')
        user.user_type=body.get('user_type')
        user.from_type=body.get('from_type', FromType.UNKNOWN)
        user.login_password=body.get('login_password','')
        user.nick_name=body.get('nick_name','')
        user.status=UserStatus.NORMAL
        user.register_date=self.now_time
        user.referee_mobile=body.get('referee_mobile','')
        user.referee_name=body.get('referee_name','')
        user.head_portrait_url=body.get('head_portrait_url','')

        #检查手机号
        if 0==len(user.mobile):
            self.set_response_error(UserErrorCode.ARGUMENT_MOBILE_ERROR)
            return False

        if not utils.tool.is_numerical_string(user.mobile):
            self.set_response_error(UserErrorCode.ARGUMENT_MOBILE_ERROR)
            return False
        
        #手机号是否已注册
#         user_dao=UserDao()
#         user=user_dao.get_user_by_mobile(user.mobile)
#         if user != None:
#             self.set_response_error(UserErrorCode.MOBILE_HAS_EXSITED)
#             return False
        
        #检查登录密码
        if len(user.login_password) < 6:
            self.set_response_error(UserErrorCode.ARGUMENT_PASSWORD_ERROR)
            return False
        
        #检查用户类型
        if not UserType.is_valid(user.user_type):
            self.set_response_error(UserErrorCode.ARGUMENT_USE_TYPE_ERROR)
            return False

        #检查推荐人        
        if 0==len(user.referee_mobile):
            self.set_response_error(UserErrorCode.ARGUMENT_REFEREE_MOBILE_ERROR)
            return False

        if not utils.tool.is_numerical_string(user.referee_mobile):
            self.set_response_error(UserErrorCode.ARGUMENT_REFEREE_MOBILE_ERROR)
            return False

        user_dao=UserDao()
        ret,referee=user_dao.get_user_by_mobile(user.referee_mobile)
        if not ret:
            self.set_response_error(UserErrorCode.SYSTEM_ERROR_DATABASE)
            return False
        if None==referee:
            self.set_response_error(UserErrorCode.REFEREE_NOT_EXSITED)
            return False
        
        if user.referee_name != referee.real_name:
            self.set_response_error(UserErrorCode.ARGUMENT_REFEREE_NAME_ERROR)
            return False
        user.referee_uid=referee.user_id
        
        return True

        
        
        
        
        
        
        
        
        
        
        