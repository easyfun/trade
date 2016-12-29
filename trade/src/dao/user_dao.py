#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2016年12月20日

@author: ASPRCK
'''
# from dao import MysqlClient
from mysql.connector import Error

class UserDao(object):
    def __init__(self,mysql_client):
        self.mysql_client=mysql_client


    def get_user_by_mobile(self, mobile):
        cursor=self.mysql_client.cursor()
        
        sql="select * from user.t_users where mobile='%s'" %(mobile,)
        try:
            cursor.execute(sql)
        
        except Error as err:#是否需要判断其它异常
            print('Error: {}'.format(err))
            return (False,None)
        
        user=None
        users=cursor.fetchall()
        for u in users:
            user=u
            break
        return (True,user)

    
    def get_user_by_user_id(self, user_id):
        cursor=self.mysql_client.cursor()
        sql="select * from user.t_user_%s where user_id='%s'" %(
            user_id[-2:],
            user_id)
        
        try:
            cursor.execute(sql)
        except Error as err:#是否需要判断其它异常
            print('Error: {}'.format(err))
            return (False,None)

        user=None
        users=cursor.fetchall()
        for u in users:
            user=u
            break
        return (True,user)
    
    def insert(self, user):
        cursor=self.mysql_client.cursor()
        
        sql='insert into user.t_user_%02d () values ()' %(
            user.user_id%100,
            )
        
        try:
            cursor.execute(sql)
        except Error as err:
            print('Error: {}'.format(err))
            return False
        
        return True
        
        
        
