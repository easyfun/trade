#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2016年12月21日

@author: ASPRCK

long最大数9223372036854775807，最大长度19
user_id纯数字串，'100'+13位数字+2位后缀
user_flow_id纯数字串，18位，'101'+13位数字+2位后缀
'''

import utils
from handler.requestex_handler import RequestExHandler
from exception.error_code import IdErrorCode
import redis_client
from handler import id

#http://domain-name/id/user_id?id_type=&suffix=
class IdHandler(RequestExHandler):
    def get(self):
        
        if not self.check_function_call(self.check_request):
            return
        
        redis=redis_client.get_redis()
        
        data=''
        if id.USER_ID==self.id_type:
            value=redis.incr(id.USER_ID_KEY)
            data='%s%013d%s' % (id.USER_ID_PREFIX, long(value), self.suffix)
        elif id.USER_FLOW_ID==self.id_type:    
            value=redis.incr(id.USER_FLOW_ID_KEY)
            data='%s%013d%s' % (id.USER_FLOW_ID_PREFIX, long(value), self.suffix)
            
        self.response['data']=data
        self.write_response()
        
        
    def check_request(self):
        self.id_type=self.get_argument('id_type', '')
        if not self.is_valid_id_type(self.id_type):
            self.set_response_error(IdErrorCode.ARGUMENT_ID_TYPE_ERROR)
            return False
            
        
        self.suffix=self.get_argument('suffix', '')
        if not utils.tool.is_numerical_string(self.suffix):
            self.set_response_error(IdErrorCode.ARGUMENT_SUFFIX_ERROR)
            return False
        
        return True
    
    def is_valid_id_type(self, id_type):
        if id.USER_ID==id_type:
            return True
        elif id.USER_FLOW_ID==id_type:
            return True
        
        return False
    
        