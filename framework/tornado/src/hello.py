#-*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web
import json

#!/usr/bin/python

import sqlite3


# db=torndb.Connection(
#     "localhost:3396",
#     "formdb",
#     "root",
#     "12345678")
# db = torndb.Connection(
#         host='db1.dqprism.com:3396',
#         database='formdb',
#         user='daqi',
#         password="7f1a45eac5985519829c929e7bbf0557",
#         time_zone='+8:00',
#         max_idle_time=180,
#         charset='utf8mb4')

conn = sqlite3.connect('test.db')
print ("Opened database successfully")
c = conn.cursor()


class MainHandler(tornado.web.RequestHandler):

    def initialize(self, conn):
        self.conn = conn

    def get(self):
        uid = self.get_argument('uid','1')
        info = self.getIdentify(uid)
        qas = self.getQuestions(uid)
        #self.write("A")
        self.render('index.html',info=info,qas=qas)

    def getIdentify(self,uid=1):
        cursor = self.conn.cursor().execute("select `id` as uid,`name`,`age`,`email`,`sex` from user where id = %s" % uid)
        for row in cursor:
            if ("%s" % row[0] == "%s" % uid):
                return {
                    'uid': uid,
                    'name': row[1],
                    'age' :row[2],
                    'email': row[3],
                    'sex': row[4],
                }
        return {
            'uid' : uid
        }

    def getQuestions(self,id='1'):
        # cursor = db.execute('select id,title from question ')
        #for row in cursor :
        #    print(row)
        l = [
            {'id':1, 'title':'QA1', 'options':[{'name':'A1','value':'1'},{'name':'B1','value':'2'}]},
            {'id':2, 'title':'QA2', 'options':[{'name':'A2','value':'1'},{'name':'B2','value':'2'}]},
            {'id':3, 'title':'QA3', 'options':[{'name':'A2','value':'1'},{'name':'B3','value':'2'}]},
        ]
        return l

class QAHandler(tornado.web.RequestHandler):

    def initialize(self, conn):
        self.conn = conn

    def get(self):
        uid = self.get_argument('uid','1')

        cursor = self.conn.cursor().execute(
            "select question_id,value from question_answer where uid = %s" % uid)
        answer = {}
        for row in cursor:
            answer[row[0]] = row[1]
        self.write(answer)
        
    def post(self):
        uid = self.get_argument('uid','1')
        body = self.request.body
        data = json.loads(body)

        c = self.conn.cursor()
        for qid in data:
            value = data[qid]
            rst = c.execute("update question_answer set value = '%s' where uid = %s and question_id = %s " % (value,uid,qid))
            print(rst.rowcount)
            if (rst.rowcount == 0):
                c.execute('insert into question_answer(uid,question_id,value) values(%s,%s,\'%s\')' % (uid,qid, value))
        self.write(data)

    def delete(self):
        uid = self.get_argument('uid','1')
        rst = self.conn.cursor().execute("delete from question_answer where uid = %s " %  uid)
        self.write({'status' : rst.rowcount > 0})

routes = [
        (r"/", MainHandler,dict(conn=conn)),
        (r"/qa", QAHandler,dict(conn=conn)),
    ]


def initDb(c):
    c.execute('''DROP TABLE IF EXISTS `question`''');

    c.execute('''CREATE TABLE `question` (
      `ID` INT PRIMARY KEY  NOT NULL,
      `title` TEXT NOT NULL,
      `type` TEXT DEFAULT NULL
    ) ;''');

    c.execute('''insert  into `question`(`id`,`title`,`type`) values (1,'Q1','select');''');
    c.execute('''DROP TABLE IF EXISTS `question_answer`;''');

    c.execute('''CREATE TABLE `question_answer` (
      `uid` int NOT NULL,
      `question_id` int NOT NULL,
      `value` TEXT NOT NULL
    ) ''');


    c.execute('''DROP TABLE IF EXISTS `question_option`;''');
    c.execute('''CREATE TABLE `question_option` (
      `id`  int PRIMARY KEY  NOT NULL,
      `name` TEXT NOT NULL,
      `value` TEXT NOT NULL,
      `question_id` int NOT NULL
    ) ''');

    c.execute('''DROP TABLE IF EXISTS `user`;''');
    c.execute('''CREATE TABLE `user` (
      `id` int NOT NULL PRIMARY KEY ,
      `name` TEXT NOT NULL,
      `age` int DEFAULT NULL,
      `email` TEXT DEFAULT NULL,
      `sex` int DEFAULT '1'
    ) ''');

    c.execute('''insert  into `user`(`id`,`name`,`age`,`email`,`sex`) values (1,'Jam',11,'ad@gmail.com',1);''');

    cursor = c.execute('select id,title from question ')
    qas = []
    for row in cursor:
        qas.append({'id':row[0],'title':row[1]})
    print (qas)

    print ("Table created successfully");



if __name__ == '__main__':

    initDb(c)
    app = tornado.web.Application(routes)
    port = 8888
    app.listen(port)
    print ("listen at ", port)
    tornado.ioloop.IOLoop.current().start()
    conn.commit()
    conn.close()
