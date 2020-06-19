# -*- coding: utf-8 -*-
import scrapy
import requests
from tutorial.items import bilibiliItem


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['www.bilibili.com']
    start_urls = ['https://www.bilibili.com/ranking']

    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
    } 
    
 #    # 配置使用pipeline
 #    ITEM_PIPELINES = {
 #    'tutorial.pipelines.bilibiliPipeline': 300,
	# }

    def parse(self, response):
    	res = response.text
    	print(res)
