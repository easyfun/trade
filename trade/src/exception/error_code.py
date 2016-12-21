#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2016年12月20日

@author: ASPRCK
'''

class UserErrorCode(object):
    ARGUMENT_MOBILE_ERROR=(100000, '请求参数错误，mobile错误')
    MOBILE_HAS_EXSITED=(100001, '此手机号已经注册')
    ARGUMENT_PASSWORD_ERROR=(100002, '请求参数错误，登录密码长度不足6位')
    ARGUMENT_USE_TYPE_ERROR=(100003, '请求参数错误，用户类型错误')
    
    
    
class IdErrorCode(object):
    ARGUMENT_SUFFIX_ERROR=(200000, '请求参数错误，后缀不是纯数字串')
