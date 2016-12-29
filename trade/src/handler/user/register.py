#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2016年12月19日

@author: ASPRCK
'''


import utils.tool
from handler.requestex_handler import RequestExHandler
from dao.user_dao import UserDao
from dao.user_flow_dao import UserFlowDao
from model.user import UserType, FromType, UserStatus
from model.user import User,UserFlow
from exception.error_code import UserErrorCode
import tornado.httpclient
import tornado.gen
import json
from exception import error_code
from datetime import datetime
from dao import MysqlClient
from handler import id

class RegisterHandler(RequestExHandler):
#     def get(self):
#         self.write('ok')

    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        user=User()
        self.mysql_client=MysqlClient()
#         if not self.check_function_call(self.check_request, user,mysql_client):
#             mysql_client.close_roll_back()
#             self.finish()
#             return
        if not self.check_request(user):
            self.finish_handler_roll_back()
            return        
        
        
        http_client=tornado.httpclient.AsyncHTTPClient()
        user_id_resp=yield tornado.web.gen.Task(http_client.fetch,
                    id.ID_URL % (id.USER_ID,user.mobile[-2:],))
        user.user_id=RequestExHandler.get_id(user_id_resp)
        if user.user_id < 0:
            self.set_response_error(UserErrorCode.CREATE_USER_ID_ERROR)
            self.finish_handler_roll_back()
            return
        
        user.update_time=datetime.date()
        user.create_time=user.update_time
        
        #插入开户请求流水
        user_flow=UserFlow()
        user_flow.set_by_user(user)
        user_flow_id_resp=yield tornado.web.gen.Task(http_client.fetch,
            id.ID_URL % (id.USER_FLOW_ID, str(user.user_id%100)))
        user_flow.flow_id=RequestExHandler.get_id(user_flow_id_resp)
        if user_flow.flow_id < 0:
            self.set_response_error(UserErrorCode.CREATE_USER_FLOW_ID_ERROR)
            self.finish_handler_roll_back()
            return
        user_flow.operation=UserFlow.REGISTER_USER_REQUEST[0]
        user_flow.remark=UserFlow.REGISTER_USER_REQUEST[1]

        user_flow_dao=UserFlowDao(self.mysql_client_flow)
        if not user_flow_dao.insert(user_flow):
            self.set_response_error(UserErrorCode.SYSTEM_ERROR_DATABASE)
            self.finish_handler_roll_back()
            return

        #插入用户表        
        user_dao=UserDao(self.mysql_client)
        if not user_dao.insert(user):
            self.set_response_error(UserErrorCode.SYSTEM_ERROR_DATABASE)
            self.finish_handler_roll_back()
            return
        
        
        #插入开户成功流水        
        user_flow_id_resp=yield tornado.web.gen.Task(http_client.fetch,
            id.ID_URL % (id.USER_FLOW_ID, str(user.user_id%100)))
        user_flow.flow_id=RequestExHandler.get_id(user_flow_id_resp)
        if user_flow.flow_id < 0:
            self.set_response_error(UserErrorCode.CREATE_USER_FLOW_ID_ERROR)
            self.finish_handler_roll_back()
            return
        user_flow.operation=UserFlow.REGISTER_USER_SUCCESS[0]
        user_flow.remark=UserFlow.REGISTER_USER_SUCCESS[1]

        if not user_flow_dao.insert(user_flow):
            self.set_response_error(UserErrorCode.SYSTEM_ERROR_DATABASE)
            self.finish_handler_roll_back()
            return

        self.finish_handler_commit()


    def check_request(self,user,mysql_client):
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

        user_dao=UserDao(mysql_client)
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

        
        
        
        
        
        
        
        
        
        
        