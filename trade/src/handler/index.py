#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web


'''
Created on 2016年12月19日

@author: ASPRCK
'''


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('easyfun平台')