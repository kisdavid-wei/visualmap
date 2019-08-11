# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VisualmapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class geoDetail(scrapy.Item):
    address = scrapy.Field()
    formatted_address = scrapy.Field()
    formatted_province = scrapy.Field()
    formatted_city = scrapy.Field()
    formatted_district = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    level = scrapy.Field()
    mark = scrapy.Field()