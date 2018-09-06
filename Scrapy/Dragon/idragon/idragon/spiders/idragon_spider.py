# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from idragon.items import IdragonItem
from scrapy.contrib.loader import ItemLoader


class IdragonSpider(scrapy.Spider):
    name = 'idragon_spider'
    allowed_domains = ['comic.dragonballcn.com']
    start_urls = ['http://comic.dragonballcn.com/list/gain_1.php?did=0-0-0&fpp=10&fid=1']

    def parse(self, response):
        item_loader = ItemLoader(item=IdragonItem(), response=response)
        item_loader.add_xpath('name', '//form[@name="frmLinkContainer"]/div/h2/text()')
        item_loader.add_css('image_url', 'div.DisplayContainer form input::attr(value)')
        item_loader.add_value('url', response.url)

        yield item_loader.load_item()
        # return ItemLoader.load_item(self)

        if response.xpath('//li[@class="NavNextItem"]/a/@href').extract()[0]:
            url = response.xpath('//li[@class="NavNextItem"]/a/@href').extract()[0]
            yield scrapy.Request("http://comic.dragonballcn.com/list/" + str(url), callback=self.parse, dont_filter=True)
