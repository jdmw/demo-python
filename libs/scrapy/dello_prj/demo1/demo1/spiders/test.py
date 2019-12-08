# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TestSpider(CrawlSpider):
    name = 'test'
    allowed_domains = ['sohu.com']
    start_urls = ['http://www.sohu.com/']

    rules = (
        Rule(LinkExtractor(allow=('http://news.sohu.com'), allow_domains=('sohu.com')), callback='parse_item',
             follow=False),
        # Rule(LinkExtractor(allow=('.*?/n.*?shtml'),allow_domains=('sohu.com')), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        i = Demo4Item()
        i['name'] = response.xpath('//div[@class="news"]/h1/a/text()').extract()
        i['link'] = response.xpath('//div[@class="news"]/h1/a/@href').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
