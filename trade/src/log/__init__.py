#!/usr/bin/env python
#-*- coding:utf-8 -*-
from tornado.log import LogFormatter
import logging
import os
import json


_FORMATTER=LogFormatter(color=False)
_FORMATTER._colors={
    logging.ERROR:u'\u0001'
}
_FORMATTER._normal=u'\u0002'

_FILENAME=os.path.join(os.curdir, 'business.log')
_HANDLER=logging.FileHandler(_FILENAME, encoding='utf-8')
_HANDLER.setFormatter(_FORMATTER)
business_logger=logging.Logger('business_log')
business_logger.addHandler(_HANDLER)

loggers={}

def get_logger(name):
    if name in loggers:
        return loggers[name]
    
    logger=logging.Logger(name)
    logger.addHandler(_HANDLER)
    loggers[name]=logger
    return logger

def logger():
    return business_logger
    
def close():
    _HANDLER.close()


def log_dumps(msg):
    return json.dumps(msg, ensure_ascii=False)