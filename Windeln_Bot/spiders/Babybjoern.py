# -*- coding: utf-8 -*-
import scrapy
from Windeln_Bot.items import WindelnBotItem


class BabybjoernSpider(scrapy.Spider):
    name = 'Babybjoern'
    allowed_domains = ['windeln.de']
    start_urls = ['https://www.windeln.com.cn/babybjoern/']

    def parse(self, response):
        item = WindelnBotItem()
        products = response.css("div.productlink-inner")
        for product in products:
            item['eans'] = product.css("a::attr(eans)").extract_first()
            item['name'] = product.css("a::attr(title)").extract_first()
            item['img'] = product.css("a > div.wrapper > img::attr(data-src)").extract_first()
            yield item

