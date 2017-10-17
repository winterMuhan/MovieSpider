# -*- coding: utf-8 -*-
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi
import codecs
import json
from sql.moviesun import movieSun
#from scrapy import item

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class JsonWithEncodingPipeline(object):
    '''保存到文件中对应的class
       1、在settings.py文件中配置
       2、在自己实现的爬虫类中yield item,会自动执行'''    
    def __init__(self):
        self.file = codecs.open('info.json', 'w', encoding='utf-8')#保存为json文件
        
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"#转为json的
        self.file.write(line)#写入文件中
        return item
    
    def spider_closed(self, spider):#爬虫结束时关闭文件
        self.file.close()


class MoviescrapyPipeline(object):
    #保存到数据库中对应的类
    def __init__(self,dbpool):
        self.dbpool = dbpool
        #self.moviesun = movieSun()
        ''' 
                                 这里注释中采用写死在代码中的方式连接线程池，可以从settings配置文件中读取，更加灵活
            self.dbpool=adbapi.ConnectionPool('MySQLdb',
                                          host='127.0.0.1',
                                          db='crawlpicturesdb',
                                          user='root',
                                          passwd='123456',
                                          cursorclass=MySQLdb.cursors.DictCursor,
                                          charset='utf8',
                                          use_unicode=False)'''  
    #scrapy默认调用
    def process_item(self, item, spider):
        '''
        query = self.dbpool.runInteraction(self._conditional_insert,item)#调用插入数据的方法
        query.addErrback(self._handle_error,item,spider)#调用异常处理办法
        '''
        return item
    
    
    @classmethod
    def from_settings(cls,settings):
        dbparams = dict(
            host = settings['MYSQL_HOST'],#读取settings中的配置
            db = settings['MYSQL_DBNAME'],
            user = settings['MYSQL_USER'],
            passwd = settings['MYSQL_PASSWD'],
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = False,
            )  
        dbpool = adbapi.ConnectionPool('MySQLdb',**dbparams)#将字典作为参数传入
        return cls(dbpool)    #将dbpool赋给这个类，self中可以得到
    
    '''
    #写入数据库
    def _conditional_insert(self,movieid,conn,item):
        sql = 'insert into moviesun(id,title,href,data) values(%s,%s,%s,%s)'
        params = (movieid,item['title'],item['href'],item['data'])
        
        conn.execute(sql,params)
        
    #错误处理方法
    def _handle_error(self,failue,item,spider):
        print '--------------database operation exception!!-----------------'
        print '-------------------------------------------------------------'
        print failue
    
    '''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
