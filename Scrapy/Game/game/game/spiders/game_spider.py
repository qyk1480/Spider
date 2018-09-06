# -*- coding: utf-8 -*-
import scrapy
from game.items import GameItem


class GameSpider(scrapy.Spider):
    name = 'game_spider'
    allowed_domains = ['http://bangumi.tv/game/']
    offset = 1
    baseUrl = 'http://bangumi.tv/game/browser?sort=rank&page='
    start_urls = [baseUrl + str(offset)]

    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        game_info = sel.xpath('//ul[@class="browserFull"]/li/div[@class="inner"]')

        # game_list = []
        for each in game_info:
            item = GameItem()
            name = each.xpath('./h3/a/text()').extract()[0]
            rank = each.xpath('./span[@class="rank"]/text()').extract()[0]
            rate = each.xpath('./p[@class="rateInfo"]/small/text()').extract()[0]

            item['name'] = name
            item['rank'] = rank
            item['rate'] = rate

            yield item
        #     game_list.append(item)
        # return game_list

        if self.offset < 161:
            self.offset += 1
            yield scrapy.Request(self.baseUrl + str(self.offset), callback=self.parse, dont_filter=True)
