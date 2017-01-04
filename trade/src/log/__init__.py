#!/usr/bin/env python
#-*- coding:utf-8 -*-
from tornado.log import LogFormatter
import logging
import os

_FORMATTER=LogFormatter(color=False)
_FORMATTER._colors={
    logging.ERROR:u'\u0001'
}
_FORMATTER._normal=u'\u0002'

_FILENAME=os.path.join(os.curdir, 'bussiness.log')
_HANDLER=logging.FileHandler(_FILENAME)
_HANDLER.setFormatter(_FORMATTER)

loggers={}

def get_logger(name):
    if name in loggers:
        return loggers[name]
    
    logger=logging.Logger(name)
    logger.addHandler(_HANDLER)
    loggers[name]=logger
    return logger
    
def close():
    _HANDLER.close()

