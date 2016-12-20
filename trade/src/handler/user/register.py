#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2016年12月19日

@author: ASPRCK
'''


import utils.tool
from handler.requestex_handler import RequestExHandler
from dao.user_dao import UserDao 
from model.user import UserType
from exception.error_code import UserErrorCode

class RegisterHandler(RequestExHandler):
#     def get(self):
#         self.write('ok')

    def post(self):
#         self.body_from_json = json.loads(self.request.body)
        
        if not self.check_function_call(self.check_request):
            return        
        
        
        
        self.write_response()
        

    def check_request(self):
        req=self.body_from_json
        resp=self.response
        
        #检查手机号
        if not utils.tool.is_numerical_string(req['mobile']):
            resp['err_code']=UserErrorCode.REQUEST_ARGUMENT_ERROR
            resp['err_msg']='请求参数错误，mobile错误'
            return False
        
        #手机号是否已注册
        user_dao=UserDao()
        user=user_dao.get_user_by_mobile(req['mobile'])
        if user != None:
            resp['err_code']=UserErrorCode.MOBILE_HAS_EXSITED
            resp['err_msg']='此手机号已经注册'
            return False
        
        #检查登录密码
        if len(req['login_password']) < 6:
            resp['err_code']=UserErrorCode.REQUEST_ARGUMENT_ERROR
            resp['err_msg']='请求参数错误，登录密码长度不足6位'
            return False
        
        #检查用户类型
        if not UserType.is_valid(req['user_type']):
            resp['err_code']=UserErrorCode.REQUEST_ARGUMENT_ERROR
            resp['err_msg']='请求参数错误，用户类型错误'
            return False
        
        return True

        
        
        
        
        
        
        
        
        
        
        