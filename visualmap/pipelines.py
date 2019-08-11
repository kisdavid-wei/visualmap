# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

class geopeline(object):
    def process_item(self, item, spider):
        if spider.name == 'gaode':
            with open('formatted_addresses.csv', 'a', encoding='utf-8') as f:
                f.write(item['address']+','+item['formatted_address']+','+ item['formatted_province']+','+ item['formatted_city']+','+ item['formatted_district']+','+ item['longitude']+','+ item['latitude']+','+
                item['level']+'\n')
        return item