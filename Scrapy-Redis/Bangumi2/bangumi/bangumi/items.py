# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
# from scrapy.loader import ItemLoader
# from scrapy.loader.processors import MapCompose, TakeFirst, Join


class BangumiItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    name_ch = scrapy.Field()
    rank = scrapy.Field()
    score = scrapy.Field()
    info = scrapy.Field()
    crawled = scrapy.Field()
    spider = scrapy.Field()

# class ExampleLoader(ItemLoader):
#     default_item_class = BangumiItem
#     default_input_processor = MapCompose(lambda s: s.strip())
#     default_output_processor = TakeFirst()
#     description_out = Join()
