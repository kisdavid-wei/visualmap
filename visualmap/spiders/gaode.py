# -*- coding: utf-8 -*-
import scrapy


class GaodeSpider(scrapy.Spider):
    name = 'gaode'
    allowed_domains = ['www.amap.com']
    start_urls = []

    def parse(self, response):
        pass
