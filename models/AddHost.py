#coding:utf-8
import os.path
import tornado.locale
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
import pymongo



class AddHost(tornado.web.RequestHandler):
    def get(self):
        self.render('addhost.html')
    def post(self, *args, **kwargs):
        username=self.get_argument('username')
        password=self.get_argument('username')
        ipaddress=self.get_argument('ipaddress')
        system=self.get_argument('system',default=None)
        mem=self.get_argument('mem')
        disk=self.get_argument('disk')
        hostname=self.get_argument('hostname')
        protocol=self.get_argument('protocol')
        group=self.get_argument('group')
        conn = pymongo.Connection("localhost", 27017)
        db=conn['hostinfo']
        zu=db[group]
        try:
            db[group].insert({"username":username,"password":password,"ipaddress":ipaddress,"system":system,
        "mem":mem,"disk":disk,"hostname":hostname,"protocol":protocol,"group":group})
            self.redirect('/')
        except Exception,ex:
            self.write(Exception,':',ex)







