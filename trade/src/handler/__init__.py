#!/usr/bin/env python
# -*- coding:utf-8 -*-
from handler.index import IndexHandler
from handler.user import register

__all__=['handlers']

handlers=[
    (r'/', IndexHandler),
    (r'/user/register', register.RegisterHandler)
]