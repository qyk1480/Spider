# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose, TakeFirst


class IdragonItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    image_url = scrapy.Field(output_processor=TakeFirst())
    # images = scrapy.Field()

# class IdragonLoader(ItemLoader):
#     default_item_class = IdragonItem
#     default_input_processor = MapCompose(lambda s: s.strip())
#     default_output_processor = TakeFirst()
#     description_out = Join()
