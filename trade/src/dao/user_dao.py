#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2016年12月20日

@author: ASPRCK
'''
from dao import MysqlClient
from mysql.connector import Error

class UserDao(MysqlClient):
    def __init__(self):
        super(UserDao,self).__init__()


    def get_user_by_mobile(self, mobile):
        cursor=self.cursor()
        
        sql="select * from user.t_users where mobile='%s'" %(mobile,)
        try:
            cursor.execute(sql)
        
        except Error as err:#是否需要判断其它异常
            print('Error: {}'.format(err))
            cursor.close()
            self.close()
            return (False,None)
        
        user=None
        users=cursor.fetchall()
        for u in users:
            user=u
            break
        cursor.close()
        self.close()
        return (True,user)

    
    def get_user_by_user_id(self, user_id):
        cursor=self.cursor()
        sql="select * from user.t_user_%s where user_id='%s'" %(
            user_id[-2:],
            user_id)
        
        try:
            cursor.execute(sql)
        except Error as err:#是否需要判断其它异常
            print('Error: {}'.format(err))
            cursor.close()
            self.close()
            return (False,None)

        user=None
        users=cursor.fetchall()
        for u in users:
            user=u
            break
        cursor.close()
        self.close()
        return (True,user)
    
    