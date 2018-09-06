# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# import scrapy
# from scrapy import signals
import json
import codecs

import pymongo
from film.settings import *


class MongodbPipeline(object):
    def __init__(self):
        host = MONGODB_HOST
        port = MONGODB_PORT
        dbname = MONGODB_DBNAME
        collection = MONGODB_COLLECTION

        client = pymongo.MongoClient(host=host, port=port)
        db = client[dbname]
        self.coll = db[collection]

    def process_item(self, item, spider):
        data = dict(item)
        self.coll.insert(data)


class JsonPipeline(object):
    def __init__(self):
        self.file = codecs.open('item.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False)+'\n\n'
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
