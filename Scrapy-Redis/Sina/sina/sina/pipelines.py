# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
import os

import json


class SinaPipeline(object):
    def process_item(self, item, spider):
        contentUrl = item['contentUrl']

        filename = contentUrl[7:-6].replace('/', '_').replace('.', '_')
        filename += '.text'

        with open(item['subFile'] + os.sep + filename, 'w') as f:
            f.write(item['content'])
            print(item['content'])
        return item


class JsonPipeline(object):
    def __init__(self):
        self.file = open('sina.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(jsontext)
        return item

    def close_spider(self, spider):
        self.file.close()
