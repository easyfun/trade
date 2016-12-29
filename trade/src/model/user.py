#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2016年12月20日

@author: ASPRCK
'''

#注册用户来源类型
class FromType(object):
    UNKNOWN=-1
    PC=0
    IOS=1
    ANDRIOD=2
    
    @staticmethod
    def is_valid(from_type):
        if FromType.PC==from_type:
            return True
        elif FromType.IOS==from_type:
            return True
        elif FromType.ANDRIOD==from_type:
            return True
        return False


#用户类型    
class UserType(object):
    INVESTOR=0
    BORROWER=1
    PLATFORM=2
    
    @staticmethod
    def is_valid(user_type):
        if UserType.INVESTOR==user_type:
            return True
        elif UserType.BORROWER==user_type:
            return True
        elif UserType.PLATFORM==user_type:
            return True
        return False


class UserStatus(object):
    NORMAL=0
    LOCKED=1
    DELETED=2
    BLACK=3
    
    @staticmethod
    def is_valid(status):
        if UserStatus.NORMAL==status:
            return True
        elif UserStatus.LOCKED==status:
            return True
        elif UserStatus.DELETED==status:
            return True
        elif UserStatus.BLACK==status:
            return True
        return False


class User(object):
    def __init__(self):
        self.user_id=None
        self.real_name=None
        self.nick_name=None
        self.login_password=None
        self.withdrawal_password=None
        self.mobile=None
        self.status=None
        self.from_type=None
        self.user_type=None
        self.register_date=None
        self.referee_uid=None
        self.referee_name=None
        self.referee_mobile=None
        self.update_time=None
        self.create_time=None
        self.head_portrait_url=None

    def __str__(self, *args, **kwargs):
        return str(self.__dict__)
#         return object.__str__(self, *args, **kwargs)

        
        
class UserFlow(object):
    REGISTER_USER_REQUEST=(0,'注册用户请求')
    REGISTER_USER_SUCCESS=(1,'注册用户成功')
    REGISTER_USER_FAIL=(2,'注册用户失败')
    
    COLUMN_NAME='flow_id,'\
                'real_name,'\
                'nick_name,'\
                'login_password,'\
                'withdrawal_password,'\
                'mobile,'\
                'from_type,'\
                'user_type,'\
                'register_date,'\
                'referee_uid,'\
                'referee_name,'\
                'referee_mobile,'\
                'operation,'\
                'remark,'\
                'create_time'
    
    
    def __init__(self):
        self.flow_id=None
        self.real_name=None
        self.nick_name=None
        self.login_password=None
        self.withdrawal_password=None
        self.mobile=None
        self.from_type=None
        self.user_type=None
        self.register_date=None
        self.referee_uid=None
        self.referee_name=None
        self.referee_mobile=None
        self.operation=None
        self.remark=None
        self.head_portrait_url=None
        self.create_time=None
        
        
    def set_by_user(self, user):    
        self.real_name=user.real_name
        self.nick_name=user.nick_name
        self.login_password=user.login_password
        self.withdrawal_password=user.withdrawal_password
        self.mobile=user.mobile
        self.from_type=user.from_type
        self.user_type=user.user_type
        self.register_date=user.register_date
        self.referee_uid=user.referee_uid
        self.referee_name=user.referee_name
        self.referee_mobile=user.referee_mobile
        self.head_portrait_url=user.head_portrait_url
        
        
        