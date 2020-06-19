# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import time

# 相当于一个容器
class maoyanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    index = scrapy.Field()
    title = scrapy.Field()
    start = scrapy.Field()
    releasetime = scrapy.Field()
    score = scrapy.Field()
    pass

class doubanItem(scrapy.Item):
	movie_name = scrapy.Field()        			
	showtime = scrapy.Field()			#上映时间
	actors = scrapy.Field()         	#主演
	director = scrapy.Field()       	#导演
	length = scrapy.Field()				#电影时长
	booking = scrapy.Field()			#票房
	score = scrapy.Field()				#豆瓣评分
	comment_num = scrapy.Field()	    #评论人数
	best_comment = scrapy.Field()		#优质评论	
	most_thumbsup_comment = scrapy.Field()	#最高点赞数评论
	best_article = scrapy.Field()		#最佳影评
	rewards = scrapy.Field()			#得奖
	detail = scrapy.Field()				#详情
	pass    

class blogItem(scrapy.Item):
	pass	

class bilibiliItem(scrapy.Item):
	today = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
	log = 'bilibili action happend'
	pass	
