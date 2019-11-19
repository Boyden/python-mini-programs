# -*- coding: utf-8 -*-

#http://www.allitebooks.com/page/1/?s=python
import scrapy
import re
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from spider.items import SpiderItem
class AlliteSpider(scrapy.Spider):
    name = "allite"
    allowed_domains = ["www.allitebooks.com"]
    start_urls = ['http://www.allitebooks.com/?s=python']
    maxnum = ""
    def parse(self, response):
        global maxnum
        item = SpiderItem()
        selector = Selector(response)
        article = selector.css('.post')
        for arc in article:            
            name = arc.xpath('.//h2[@class="entry-title"]//text()').extract_first()
            link = arc.css('.entry-title a::attr(href)').extract_first()
            author = arc.xpath('.//h5[@class="entry-author"]/a/text()').extract()
            description = arc.xpath('.//div[@class="entry-summary"]/p/text()').extract_first()
            authors = ''
            for eachAuthor in author:
                eachAuthor += ' '
                authors += eachAuthor
            item['name'] = name
            item['link'] = link
            item['author'] = authors
            item['description'] = description
            yield item
        url = 'http://www.allitebooks.com/page'
        digits = re.findall(r'/(\d+)/', response.url)
        digit = 0
        if bool(self.maxnum) is False:
            self.maxnum = selector.css("#content .pagination a:last-child").xpath(".//text()").extract_first()
            self.maxnum = int(self.maxnum)

        print("\nmaxnum:" + str(self.maxnum) + '\n')
        if digits:
            digit = int(digits[0]) + 1
            nextURL = url + '/' + str(digit) + '/?s=python'
        else:
            nextURL = url + '/2/?s=python'
        if digit <= self.maxnum:
            print("\nnextURL:" + nextURL + "\n")
            yield scrapy.Request(nextURL, callback=self.parse)
        
