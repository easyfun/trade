#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Created on 2016年12月20日

@author: ASPRCK
'''

digits=('0','1','2','3','4','5','6','7','8','9')

def is_numerical_string(string):
    if string==None:
        return False
    
#     if string=='':
#         return False
    
    for s in string:
        if s not in digits:
            return False
        
    return True

