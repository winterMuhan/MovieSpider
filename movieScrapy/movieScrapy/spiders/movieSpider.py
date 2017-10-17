 #-*-coding:utf-8-*-
'''
Created on 2017年7月19日

@author:W慕寒
'''
from scrapy.http import Request
from urlparse import urljoin
from movieScrapy.items import MoviescrapyItem
from scrapy.spiders import Spider
#使用xpath
from scrapy.selector import Selector
from lxml import etree
from bs4 import BeautifulSoup as bs
from sql.moviesun import movieSun
import requests
import time

count = 0
class movie(Spider):
    #define a name for spider
    name = 'movieSpider'
    start_urls = ['http://www.ygdy8.com/html/gndy/dyzz/list_23_1.html']
    
    #base_url = 'http://www.ygdy8.com'
    def __init__(self):
        self.movieSun = movieSun()
        
    def parse(self, response):
        global count
        base_url = 'http://www.ygdy8.com/html/gndy/dyzz/'
        html = response.body
        item = MoviescrapyItem()
        #selector = Selector(response)
        #bs解析html
        soup = bs(html,'html.parser')
        datas = soup.find('div',class_="co_content8")
        movie_urls = datas.find('select').find_all('option')
        #根据首页获取到的链接，爬取数据
        for movie_url in movie_urls:
            url = base_url+movie_url.get('value')
            headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
            movie_html = requests.get(url, headers=headers).content
            #print movie_html
            movie_soup = bs(movie_html,'lxml')
            movie_datas = movie_soup.find('div',class_="co_content8").find('ul')
            tables = movie_datas.find_all('table')
            
            for eachtable in tables:
                item['title']=eachtable.find('a').get_text().decode('UTF-8').encode('UTF-8')
                item['href']=urljoin(base_url,eachtable.find('a').get('href'))
                item['data']=eachtable.find('font').get_text().decode('UTF-8').encode('UTF-8')
                #向数据库插入数据
                count+=1
                self.movieSun.testInsert(count,item['title'], item['href'],item['data'])
            print '收集到%d条数据！'%count
                #yield item
        
                 
            
    
    
