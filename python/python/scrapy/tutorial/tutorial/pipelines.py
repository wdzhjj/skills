# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 定义Item Pipeline的实现 实现数据的清洗，储存，验证。

import time
# 导入访问MySQL的模块
import pymysql.cursors

class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class bilibiliPipeline(object):
	# 定义构造器，初始化要写入的条件
	def __init__(self):
		self.conn = pymysql.connect(
            host='116.62.9.18',  # 数据库地址
            port=3306,  # 数据库端口
            db='blog',  # 数据库名
            user='root',  # 数据库用户名
            passwd='lgh118117',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)
		self.cur = self.conn.cursor()
	# 重写 close_spider 回调方法，用户关闭数据库资源	
	def close_spider(self,spider):
		print('----------关闭数据库资源----------')
		self.cur.close()
		self.conn.close()
	# 写入数据库的逻辑
	def process_item(self, item, spider):
		sql = "insert into log(create_at,action) values('test','test')"
		print(sql)
		self.cur.execute(sql)
		self.conn.commit()
		return item

#图片下载中间件

# class ImagespiderPipeline(ImagesPipeline):
# 	def get_media_request(self, item, info):
# 		for image_url in item['imgurl']:
# 			yield Request(image_url)