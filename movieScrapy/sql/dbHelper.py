#!/user/local/bin/python2.7
# -*- coding:utf-8 -*-
import MySQLdb
from scrapy.utils.project import get_project_settings #����seetings����

class DBHelper():
    
    '''这个类也是读取settings中的配置，自行修改代码进行操作'''
    def __init__(self):
        self.settings=get_project_settings() #获取setting中mysql的配置
        
        self.host=self.settings['MYSQL_HOST']
        self.port=self.settings['MYSQL_PORT']
        self.user=self.settings['MYSQL_USER']
        self.passwd=self.settings['MYSQL_PASSWD']
        self.db=self.settings['MYSQL_DBNAME']
    
    #连接到mysql
    def connectMysql(self):
        conn=MySQLdb.connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             passwd=self.passwd,
                             #db=self.db,
                             charset='utf8') 
        return conn
    #连接到指定的数据库
    def connectDatabase(self):
        conn=MySQLdb.connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             passwd=self.passwd,
                             db=self.db,
                             charset='utf8') #指定编码
        return conn   
    
    #创建数据库
    def createDatabase(self):
        '''因为创建数据库直接修改settings中的配置MYSQL_DBNAME即可，所以就不需要传sql语句了'''
        #链接MySQL
        conn = self.connectMysql()
        sql="create database if not exists "+self.db
        cur=conn.cursor()
        cur.execute(sql)#ִ执行sql语句
        cur.close()
        conn.close()
    
    #创建表
    def createTable(self,sql):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()
    #查询数据
    def select(self,sql,params=None):#为查询条件设置默认值为空
        conn=self.connectDatabase()
        
        cur=conn.cursor();
        cur.execute(sql,params)
        data = cur.fetchall()
        conn.commit()#提交数据
        cur.close()
        conn.close()
        return data
        
           
    
    #向表中插入数据
    def insert(self,sql,*params):#传入的是一个元组，所以加*
        conn=self.connectDatabase()
        
        cur=conn.cursor();
        cur.execute(sql,params)
        conn.commit()#提交数据
        cur.close()
        conn.close()
    #更新数据
    def update(self,sql,*params):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql,params)
        conn.commit()#ע��Ҫcommit
        cur.close()
        conn.close()
    
    #删除数据
    def delete(self,sql,*params):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql,params)
        conn.commit()
        cur.close()
        conn.close()
        
    def deleteall(self,sql):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        