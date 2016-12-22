#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2016年12月20日

@author: ASPRCK
'''
from dao import MysqlClient
from mysql.connector import ProgrammingError

class UserDao(MysqlClient):
    def __init__(self):
        super(UserDao,self).__init__()


    def get_user_by_mobile(self, mobile):
        cursor=self.cursor()
        
        sql="select * from user.t_user_%s where mobile='%s'" %(
            mobile[-2:],
            mobile)
        try:
            cursor.execute(sql)
        
        except ProgrammingError as err:
            print('Error: {}'.format(err))
            return None
        
        user=None
        users=cursor.fetchall()
        for u in users:
            user=u
            break
        cursor.close()
        return user

    
    def get_user_by_user_id(self, user_id):
        cursor=self.cursor()
        sql="select * from user.t_user_%s where user_id='%s'" %(
            user_id[-2:],
            user_id)
        cursor.execute(sql)
        user=None
        users=cursor.fetchall()
        for u in users:
            user=u
            break
        cursor.close()
        return user
    
    