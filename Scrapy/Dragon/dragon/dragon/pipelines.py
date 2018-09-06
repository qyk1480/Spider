# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# import scrapy
# from scrapy import signals
# import json, codecs


# class DragonPipeline(object):
#     def process_item(self, item, spider):
#         return item

# class JsonWithEncodingDragonPipeline(object):
#     def __init__(self):
#         self.file = codecs.open('item.json','w',encoding='utf-8')

#     def process_item(self,item,spider):
#         line = json.dumps(dict(item),ensure_ascii=False)+'\n\n'
#         self.file.write(line)
#         return item

#     def spider_closed(self,spider):
#         self.file.close()

import os
import scrapy

from dragon.settings import IMAGES_STORE as images_store
from scrapy.pipelines.images import ImagesPipeline


class DragonPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        link = item['link'][0]
        yield scrapy.Request(link)

    def item_completed(self, results, item, info):
        for ok, x in results:
            if ok:
                image_path = [x['path']]
        # image_path = [x["path"] for ok, x in results if ok]

        os.rename(images_store + image_path[0], images_store + str(item['title'][0]))
        return item
