# -*- coding: utf-8 -*-
import scrapy
from Windeln_Bot.items import WindelnBotItem



class BrandsspiderSpider(scrapy.Spider):
    name = 'brandsspider'
    allowed_domains = ['windeln.de']
    start_urls = ['https://www.windeln.de/alle-marken/']

    def parse(self, response):
        urls = response.css('div.list>a.list-item::attr(href)').extract()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_items)



    def parse_items(self,response):
        item = WindelnBotItem()
        item['name'] = response.css('h3.name::text')[0].extract()
        item['eans'] = response.css('a.product-link::attr(eans)')[0].extract()
        item['img'] = response.css('div.wrapper > img::attr(data-src)')[0].extract()
        yield item






