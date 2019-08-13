# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
import json
from visualmap.items import geoDetail
import configparser

class GaodeSpider(scrapy.Spider):
    name = 'gaode'
    allowed_domains = ['www.amap.com']
    start_urls = []

    config = configparser.ConfigParser()
    path = 'app.config'
    config.read(path)
    gaodekey = config.get('key', 'gaodekey')

    with open('addresses.txt', 'r', encoding='utf-8') as f:
        address = f.readline()
        address = address[:-1]
        while address != '':
            start_urls.append('https://restapi.amap.com/v3/geocode/geo?key='+gaodekey+'&address='+ urllib.parse.quote(address))
            address = f.readline()
            address = address[:-1]
            print(address)

    with open('./static/formatted_addresses.csv', 'w', encoding='utf-8') as f:
        f.write('address' + ',' + 'formatted_address' + ',' + 'formatted_province' + ',' +
            'formatted_city' + ',' + 'formatted_district'+ ',' +'longitude' + ',' +
                    'latitude' + ',' +
                'level'+ '\n')

    def parse(self, response):
        geo = json.loads(response.body)
        if geo['status'] == '1' and geo['count'] == '1':
            item = geoDetail()
            item['address'] = urllib.parse.unquote(str(response.url.split('address=')[1]))
            item['formatted_address'] = geo["geocodes"][0]["formatted_address"]
            item['formatted_province'] = geo["geocodes"][0]["province"]
            item['formatted_city'] = geo["geocodes"][0]["city"]
            if type(geo["geocodes"][0]["district"]) == type([]):
                item['formatted_district'] = ''
            else:
                item['formatted_district'] = geo["geocodes"][0]["district"]
            location = geo["geocodes"][0]["location"]
            if len(location.split(',')) > 1:
                item['longitude'] = location.split(',')[0]
                item['latitude'] = location.split(',')[1]
            item['level'] = geo["geocodes"][0]["level"]
            yield item

