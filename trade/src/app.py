#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tornado.web
import tornado.httpserver
import tornado.ioloop
import handler
import log

from tornado.options import define,options
define('port', default=8080, type=int, help='run on the given port')


def main():
    options.parse_command_line()
    app=tornado.web.Application(handlers=handler.handlers)
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    log.close()
    
if '__main__'==__name__:
    main()