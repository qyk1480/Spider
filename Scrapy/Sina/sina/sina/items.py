# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    # define the fields for your item here like:
    parentName = scrapy.Field()
    parentUrl = scrapy.Field()

    subName = scrapy.Field()
    subUrl = scrapy.Field()

    subFile = scrapy.Field()

    contentUrl = scrapy.Field()

    title = scrapy.Field()
    content = scrapy.Field()
