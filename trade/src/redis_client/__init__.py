#!/usr/bin/env python
#-*- coding:utf-8 -*-

import redis

redis_connection_pool=redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)

def get_redis():
    return redis.Redis(connection_pool=redis_connection_pool)