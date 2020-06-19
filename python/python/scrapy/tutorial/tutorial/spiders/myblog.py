# -*- coding: utf-8 -*-
import scrapy


class MyblogSpider(scrapy.Spider):
    name = 'myblog'
    allowed_domains = ['127.0.0.11']
    start_urls = ['http://127.0.0.11/detail/id/1']

    def parse(self, response):
        print(response.text)
