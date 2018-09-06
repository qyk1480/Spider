# -*- coding: utf-8 -*-
import scrapy
from jsoncity.items import JsoncityItem
import json


class JsonSpider(scrapy.Spider):
    name = 'json_spider'
    allowed_domains = ['https://www.lagou.com/lbs/getAllCitySearchLabels.json']
    start_urls = ['https://www.lagou.com/lbs/getAllCitySearchLabels.json/']

    def parse(self, response):
        content = json.loads(response.body)
        data = content['content']['data']['allCitySearchLabels']

        print(data['A'])
        for i in range(65, 91):
            for city in data[chr(i)]:
                for each in city:
                    item = JsoncityItem()

                    item['cityid'] = city['id']
                    item['name'] = city['name']
                    item['parentId'] = city['parentId']
                    item['code'] = city['code']

                    yield item
