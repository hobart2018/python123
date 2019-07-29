# -*- coding: utf-8 -*-
import scrapy
import re

class StockSpider(scrapy.Spider):
    name = 'stock'
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            try:
                stock = re.findall(r'[s][hz]\d{6}', href)[0]
                url = 'https://gupiao.baidu.com/stock/' + stock +'.html'
                yield scrapy.Request(url, callback = self.parse_stock)
            except:
                continue


