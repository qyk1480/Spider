# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JsoncityItem(scrapy.Item):
    # define the fields for your item here like:
    cityid = scrapy.Field()
    name = scrapy.Field()
    parentId = scrapy.Field()
    code = scrapy.Field()
