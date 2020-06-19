import scrapy
#需要引入数据容器
from tutorial.items import maoyanItem

class maoyanSpider(scrapy.Spider):
	name = 'maoyan'
	allowed_domains = ['manyan.com']
	start_urls = ['http://maoyan.com/board/7','http://maoyan.com/board/6']

	def parse(self,response):
		dl = response.css('.board-wrapper dd')
		for dd in dl:
			item = maoyanItem()
			item['index'] = dd.css('.board-index::text').extract_first()
			item['title'] = dd.css('.name a::text').extract_first()
			item['star'] = dd.css('.star::text').extract_first()
			item['releasetime'] = dd.css('.releasetime::text').extract_first()
			item['score'] = dd.css('.integer::text').extract_first()+dd.css('.fraction::text').extract_first()
			yield item