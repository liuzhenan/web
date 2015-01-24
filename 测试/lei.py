# -*- coding:utf-8 -*-

class OOO(object):
    def __init__(self, value):
        self.value=value
    
if __name__ == "__main__":
    a=OOO(100)
    print a.value
    del a.value
    #print a.value

    print '############################'

    b=OOO(50)
    print b.value
    del b.value
    #print b.value
