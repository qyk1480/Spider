# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
import codecs
import requests
from idragon.settings import IMAGES_STORE
import os


class JsonPipeline(object):
    def __init__(self):
        self.file = codecs.open('item.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False)+'\n\n'
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


class IdragonPipeline(object):
    def process_item(self, item, spider):
        if 'image_url' in item:
            if not os.path.exists(IMAGES_STORE):
                os.mkdir(IMAGES_STORE)
            os.chdir(IMAGES_STORE)
            with open(item['name'], 'wb') as f:
                image = requests.get(item['image_url'], stream=True)
                for block in image.iter_content(1024):
                    if not block:
                        break
                    f.write(block)

        return item
