#!/usr/bin/env python
#-*- coding:utf-8 -*-

import mysql.connector

class MysqlClient(object):
    _HOST='127.0.0.1' 
    _USER='root'
    _PASSWORD='easyfun'
    _POOL_SIZE=10

    def __init__(self):
        self.connection=None
        self.cursor=None
    
    def connect(self):
        self.connection=mysql.connector.connect(
            host=MysqlClient._HOST,
            user=MysqlClient._USER,
            password=MysqlClient._PASSWORD,
            pool_size=MysqlClient._POOL_SIZE)
        
    def cursor(self):
        if not self.connection:
            self.connect()
        if not self.cursor:
            self.cursor=self.connection.cursor(dictionary=True)
        return self.cursor
        
    def close(self):
        self.cursor.close()
        self.connection.close()
            
    def close_commit(self):
        self.cursor.close()
        self.connection.commit()
        self.connection.close()
        
    def close_roll_back(self):
        self.cursor.close()
        self.connection.rollback()
        self.connection.close()
            
            
    