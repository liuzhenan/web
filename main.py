#coding:utf-8
import os.path
import os
import base64
from uuid import uuid4
import tornado.locale
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
import pymongo

from models.AddHost import *
from models.Index import *


define("port",default=3838,help="run on the localhost",type=int)
class Application(tornado.web.Application):
    def __init__(self):
        handlers=[(r'/', IndexHandler),
                  (r'/login', LoginHandler),
                  (r'/logout', LogoutHandler),
                  (r'/addhost', AddHost)]
        settings =dict(
        template_path=os.path.join(os.getcwd(),"templates"),
        #static_path="D:/projects1/gothonweb/bin/static",
        #static_path=os.path.join(os.path.dirname(__file__),"templates"),
        static_path=os.path.join(os.getcwd(),"templates"),
        cookie_secret="bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
        xsrf_cookies=True,
        login_url="/login",
        debug = True)
        conn = pymongo.Connection("localhost", 27017)
        self.db = conn["user"]
        tornado.web.Application.__init__(self, handlers, **settings)



if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()