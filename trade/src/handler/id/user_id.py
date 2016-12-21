#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2016年12月21日

@author: ASPRCK

long最大数9223372036854775807，最大长度19
user_id纯数字串，'100'+13位数字+2位后缀
'''

import utils
from handler.requestex_handler import RequestExHandler
from exception.error_code import IdErrorCode
import redis_client
from handler import id

#http://domain-name/id/user_id?suffix=
class UserIdHandler(RequestExHandler):
    def get(self):
        
        if not self.check_function_call(self.check_request):
            return
        
        redis=redis_client.get_redis()
        id_value=redis.incr(id.USER_ID_KEY)
        user_id='%s%013d%s' % (id.USER_ID_PREFIX, long(id_value), self.suffix)
        
        self.response['data']=user_id
        self.write_response()
        
        
    def check_request(self):
        self.suffix=self.get_argument('suffix', '')
        if not utils.tool.is_numerical_string(self.suffix):
            self.set_response_error(IdErrorCode.ARGUMENT_SUFFIX_ERROR)
            return False
        
        return True
    
    
    
        