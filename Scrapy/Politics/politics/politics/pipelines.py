# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json


class PoliticsPipeline(object):
    def __init__(self):
        self.file = open('politics.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(jsontext)
        return item

    def close_spider(self, spider):
        self.file.close()
