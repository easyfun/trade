#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2016年12月19日

@author: ASPRCK
'''
import tornado.web

class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        print(self.path_args)
        self.write('ok')