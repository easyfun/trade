#!/usr/bin/env python
#-*- coding:utf-8 -*-

# import mysql.connector
from model.user import UserFlow

# def test_mysql():
#     conn=mysql.connector.connect(
#         host='127.0.0.1',
#         user='root',
#         password='easyfun',
#         database='user')
#     
#     cursor=conn.cursor(dictionary=True)
#     sql='insert into test.user (uid,mobile,name) values (1,"1351729","liyu")'
#     cursor.execute(sql)
#     # rows=cursor.fetchall()
#     
#     sql='select * from test.user limit 0,3'
#     cursor.execute(sql)
#     rows=cursor.fetchall()
#     print(rows)
#     
#     # conn.commit()

print('hello')
print(UserFlow.COLUMN_NAME)



