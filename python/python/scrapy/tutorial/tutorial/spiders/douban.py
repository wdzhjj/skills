# -*- coding: utf-8 -*-
import scrapy

import requests
from bs4 import BeautifulSoup
from lxml import etree

from tutorial.items import doubanItem
import json


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    # allowed_domains = ['m.douban.com']
    start_urls = [
    	# 'https://movie.douban.com/subject/5322596/',
    	# 'http://lab.scrapyd.cn/page/*/',
    	# 'https://www.baidu.com'
		'https://m.douban.com/rexxar/api/v2/gallery/subject_feed?start=0&count=4&subject_id=1298624&ck=null'
    ]

    #设置浏览器用户代理
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    'Referer':'https://movie.douban.com/subject/48415151/'
    } 

    # def start_requests(self):
    # 	urls = [
    # 		'https://movie.douban.com/subject/5322596/',
    # 		'http://lab.scrapyd.cn/page/1/',
    # 	]
    # 	for url in urls:
    # 		yield scrapy.Request(url=url,callback=self.parse)

    #设置url  回调方法  请求头   有默认值
    def start_requests(self):
        return [scrapy.Request(url=self.start_urls[0], callback=self.parse, headers=self.headers)]
    
    def parse(self, response):
    	res = response.text
    	res = json.loads(res)
    	print(res)

    	movie_name = res['items']['topic']['title']

    	comment_num = res['items']['topic']['focused_subject']['rating']['count']
    	score =  res['items']['topic']['focused_subject']['rating']['value']

    	detail = res['items']['topic']['card_subtitle']

    	print(movie_name)

    	# f = open("debug.txt",'w')
    	# f.write(res)









