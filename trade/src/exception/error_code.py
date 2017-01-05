#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2016年12月20日

@author: ASPRCK
'''

SUCCESS_CODE=0

class UserErrorCode(object):
    ARGUMENT_MOBILE_ERROR=(100000, u'请求参数错误，手机号错误')
    MOBILE_HAS_EXSITED=(100001, u'此手机号已经注册')
    ARGUMENT_PASSWORD_ERROR=(100002, u'请求参数错误，登录密码长度不足6位')
    ARGUMENT_USE_TYPE_ERROR=(100003, u'请求参数错误，用户类型错误')
    CREATE_USER_ID_ERROR=(100004, u'创建用户id失败')
    ARGUMENT_REFEREE_MOBILE_ERROR=(100005, u'请求参数错误，推荐人手机号错误')
    ARGUMENT_REFEREE_NAME_ERROR=(100006, u'请求参数错误，推荐人姓名错误')
    REFEREE_NOT_EXSITED=(100007, u'请求参数错误，推荐人不存在')
    SYSTEM_ERROR_DATABASE=(100008, u'系统错误，数据库服务异常')
    CREATE_USER_FLOW_ID_ERROR=(100004, u'创建用户流水id失败')
    
    
    
class IdErrorCode(object):
    ARGUMENT_ID_TYPE_ERROR=(200000, u'请求参数错误，id_type类型错误')
    ARGUMENT_SUFFIX_ERROR=(200000, u'请求参数错误，后缀不是纯数字串')
