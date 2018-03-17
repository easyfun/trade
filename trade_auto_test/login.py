# /usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
from urllib import request

def login():
    with request.urlopen('https://www.baidu.com') as f:
        data=f.read()
        print('Status: ', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', data.decode('utf-8'))

if __name__ == '__main__':
    login()