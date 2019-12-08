#-*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web
import torndb

db=torndb.Connection(
    "localhost:3396",
    "name",
    "user",
    "pass")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        uid = self.get_argument('uid','1')
        info = self.getIdentify(uid)
        qas = self.getQuestions(uid)
        self.render('index.html',info=info,qas=qas)

    def getIdentify(self,uid='1'):
        return {
            'uid':uid,
            'name' :'Hurry',
            'sex' : '1',
            'email' : '1231@gmail.com',
        }
    def getQuestions(self,id='1'):
        rst = db.query('select id,title from question ')
        l = [
            {'id':1, 'title':'QA1', 'options':[{'name':'A1','value':'1'},{'name':'B1','value':'2'}]},
            {'id':2, 'title':'QA2', 'options':[{'name':'A2','value':'1'},{'name':'B2','value':'2'}]},
            {'id':3, 'title':'QA3', 'options':[{'name':'A2','value':'1'},{'name':'B3','value':'2'}]},
        ]
        return rst 


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        uid = self.get_argument('uid','1')
        return {
            'uid':uid,
            'name' :'Hurry',
            'sex' : '1',
            'email' : '1231@gmail.com',
        }
        
    def post(self):
        uid = self.get_argument('uid','1')
        return [
            {'id':1, 'title':'QA1', 'options':[{'name':'A1','value':'1'},{'name':'B1','value':'2'}]},
            {'id':2, 'title':'QA2', 'options':[{'name':'A2','value':'1'},{'name':'B2','value':'2'}]},
            {'id':3, 'title':'QA3', 'options':[{'name':'A2','value':'1'},{'name':'B3','value':'2'}]},
        ]
        
        
        
routes = [
        (r"/", MainHandler),
    ]

if __name__ == "__main__":
    app = tornado.web.Application(routes)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    