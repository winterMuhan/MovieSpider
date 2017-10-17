#!/user/local/bin/python2.7
# -*- coding:utf-8 -*-
from dbHelper import DBHelper

class movieSun(object):
    def __init__(self):
        self.dbHelper = DBHelper()
        
    #测试创建数据库（settings配置文件中的MYSQL_DBNAME,直接修改settings配置文件即可）
    def testCreateDatebase(self):
        self.dbHelper.createDatabase() 
    #测试创建表
    def testCreateTable(self):
        sql="create table moviesun(id int primary key auto_increment,title varchar(100),href varchar(100),data varchar(500))"
        self.dbHelper.createTable(sql)
    #测试插入
    def testInsert(self,movieid,title,href,data):
        sql="insert into moviesun(id,title,href,data) values(%s,%s,%s,%s)"
        params=(movieid,title,href,data,)
        self.dbHelper.insert(sql,*params) #  *表示拆分元组，调用insert（*params）会重组成元组
    #更新数据
    def testUpdate(self,title,href,data,movie_id):
        sql="update moviesun set title=%s,href=%s,data=%s where id=%s"
        params=(title,href,data,movie_id,)
        self.dbHelper.update(sql,*params)
    #删除数据
    def testDelete(self,movie_id):
        sql="delete from moviesun where id=%s"
        params=(movie_id,)
        self.dbHelper.delete(sql,*params)
        
    #删除全部数据
    def testDeleteall(self):
        sql="delete from moviesun"
        #params=(movie_id,)
        self.dbHelper.deleteall(sql)
        
    def testSelectall(self):
        sql = 'select title from moviesun where 1=1'
        
        return self.dbHelper.select(sql)
        
'''       
if __name__=="__main__":
    testDBHelper=movieSun()
    #testDBHelper.testCreateDatebase()  #执行测试创建数据库
    #testDBHelper.testCreateTable()     #执行测试创建表
    #testDBHelper.testInsert()          #执行测试插入数据
    #testDBHelper.testUpdate()          #执行测试更新数据
    #testDBHelper.testDelete()          #执行测试删除数据
'''       
        
        
        
