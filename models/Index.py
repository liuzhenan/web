#coding:utf-8
import tornado.web
#初始化，复写get_current_user()方法来返回当前用户。
class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")

#登陆验证
class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html',errmgs=None)
    def post(self):

        username=self.get_argument('user')
        password=self.get_argument('passwd')
        sysadmin = self.application.db.root
        a=sysadmin.find_one({str(username):str(password)})
        #print a
        if a:
            self.set_secure_cookie("username", self.get_argument("user"))
            self.set_secure_cookie("password", self.get_argument("passwd"))
            self.render('index.html',user=self.get_argument("user"))
        else:
            #self.write('<script>alert(\'用户名或密码错误\')</script>')
            self.render('login.html',errmgs='<script>alert(\'用户名或密码错误\')</script>')


#用户注销
class LogoutHandler(BaseHandler):
    def get(self):
        #if (self.get_argument("logout", None)):
            self.clear_cookie("username")
            self.clear_cookie("password")
            self.redirect("/login")


#如果有cookie则直接登陆到平台
class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('index.html', user=self.current_user,errmgs=None)
