#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2016年12月29日

@author: ASPRCK
'''
from mysql.connector import Error

class UserFlowDao(object):
    def __init__(self,mysql_client):
        self.mysql_client=mysql_client


    def insert(self, user_flow):
        cursor=self.mysql_client.cursor()
        
        sql='insert into user.t_user_flow_%02d (%s) values ()' %(
            user_flow.user_id%100,
            )
        
        try:
            cursor.execute(sql)
        except Error as err:
            print('Error: {}'.format(err))
            return False
        
        cursor.fetchall()
        return True
        
        
        
