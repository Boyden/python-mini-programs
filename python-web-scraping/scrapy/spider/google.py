# -*- coding: utf-8 -*-


#class GoogleSpider(scrapy.Spider):
#    name = "google"
#    allowed_domains = ["http://quotes.toscrape.com/page/1/"]
#    start_urls = ['http://quotes.toscrape.com/page/1/','http://quotes.toscrape.com/page/2/','http://quotes.toscrape.com/page/3/']

#    def parse(self, response):
#    	for h3 in response.xpath('//h3').extract():
#    		yield self.logger.info(h3)

#    	for url in response.xpath('//a/@href').extract():
#    		yield scrapy.Request(url, callback=self.parse)
#    def start_requests(self):
#    	yield scrapy.Request('http://quotes.toscrape.com/page/1/', self.parse)
#    	yield scrapy.Request('http://quotes.toscrape.com/page/2/', self.parse)
#    	yield scrapy.Request('http://quotes.toscrape.com/page/3/', self.parse)
from scrapy.spiders import XMLFeedSpider
import scrapy
class TestItem(scrapy.Item):
	id = scrapy.Field()
	name = scrapy.Field()
	description = scrapy.Field()
class MySpider(XMLFeedSpider):
	name = "google"
	allowed_domains = ['http://quotes.toscrape.com/page/1/']
	start_urls = ['http://quotes.toscrape.com/page/1/','http://quotes.toscrape.com/page/2/','http://quotes.toscrape.com/page/3/']
	iterator = 'iternodes'
	itertag = 'item'
	def parse_node(self, response, node):
		self.logger.info('Hi, this is a <%s> node!:%s', self.itertag, ''.join(node.extract()))
		item = TestItem()
		item['id'] = node.xpath('@id').extract()
		item['name'] = node.xpath('name').extract()
		item['description'] = node.xpath('description').extract()
		return item