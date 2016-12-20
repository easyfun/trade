#!/usr/bin/env python
#-*- coding:utf-8 -*-

import mysql.connector

class MysqlClient(object):
    _HOST='127.0.0.1' 
    _USER='user'
    _PASSWORD='easyfun'
    _POOL_SIZE=10

    def __init__(self):
        self.connection=None
    
    def connect(self):
        self.connection=mysql.connector.connect(
            host=MysqlClient._HOST,
            user=MysqlClient._USER,
            password=MysqlClient._PASSWORD,
            pool_size=MysqlClient._POOL_SIZE)
        
    def cursor(self):
        self.connect()
        return self.connection.cursor(dictionary=True)
        
    def close(self):
        self.connection.close()