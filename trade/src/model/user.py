#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2016年12月20日

@author: ASPRCK
'''

#注册用户来源类型
class FromType(object):
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
        elif UserType.ANDRIOD==user_type:
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
        
        
class UserFlow(object):
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
        self.create_time=None