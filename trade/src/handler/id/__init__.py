#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2016年12月21日

@author: ASPRCK

long最大数9223372036854775807，最大长度19
user_id纯数字串，18位，'100'+13位数字+2位后缀
user_flow_id纯数字串，18位，'101'+13位数字+2位后缀
'''

USER_ID_KEY='id.user_id'
USER_ID_PREFIX='100'

USER_FLOW_ID_KEY='id.user_flow_id'
USER_FLOW_ID_PREFIX='101'


USER_ID='user_id'
USER_FLOW_ID='user_flow_id'

ID_URL='http://127.0.0.1:8080/id?id_type=%s&suffix=%s'