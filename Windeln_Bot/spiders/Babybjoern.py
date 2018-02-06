# -*- coding: utf-8 -*-
import scrapy
from Windeln_Bot.items import WindelnBotItem



class BrandsspiderSpider(scrapy.Spider):
    name = 'Babybjoern'
    allowed_domains = ['windeln.de']
    start_urls = ['https://www.windeln.de/babybjoern/']

    def parse(self,response):
        item = WindelnBotItem()
        item['name'] = response.css('h3.name::text')[0].extract()
        item['eans'] = response.css('a.product-link::attr(eans)')[0].extract()
        item['img'] = response.css('div.wrapper > img::attr(data-src)')[0].extract()
        yield item


    






