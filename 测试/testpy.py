#coding:utf-8
import uuid
import base64
import chardet
import os
import time
import hashlib


a = os.urandom(16)
b = time.time()
#print chardet.detect(a)
#print a.decode('windows-1251').encode('utf-8')
#print uuid.uuid4()


#print hashlib.sha1("%s%s" %(a,b)).hexdigest()

#aa={}
#bb={'key1':'hi','key2':'hello'}

class xxoo(dict):
    def __missing__(self,key):
        return 2
    def __getitem__(self, key):
        return self.goodlist[key]
  def __setitem__(self, key, value):
    super(xxoo, self).__setitem__(key, value)
nan=xxoo()
#print nan.goodlist['first']


print nan['second']



