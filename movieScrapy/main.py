#-*-coding:utf-8-*-
'''
Created on 2017年7月19日

@author:W慕寒
'''
from scrapy import cmdline
from sql.moviesun import movieSun

if __name__ == "__main__":
    movie = movieSun()
    #movie.testCreateDatebase()
    #movie.testCreateTable()
    #首先清空表中的全部数据
    movie.testDeleteall()
    #运行爬虫，将数据添加到mysql数据库
    cmdline.execute("scrapy crawl movieSpider".split())
    for title in movie.testSelectall():
        print title[0]
    

