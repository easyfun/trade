#!/usr/bin/env python
# -*- coding:utf-8 -*-
from handler.index import IndexHandler
from handler.user import register
from handler.id import user_id

__all__=['handlers']

handlers=[
    (r'/', IndexHandler),
    
    (r'/user/register', register.RegisterHandler),
    
    (r'/id/user_id', user_id.UserIdHandler)
]