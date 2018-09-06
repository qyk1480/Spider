# -*- coding: utf-8 -*-
import scrapy
from game.items import GameItem


class GsoupSpiderSpider(scrapy.Spider):
    name = 'gsoup_spider'
    allowed_domains = ['bangumi.tv/game/']
    offset = 1
    baseUrl = 'http://bangumi.tv/game/browser?sort=rank&page='
    start_urls = [baseUrl + str(offset)]

    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        game_info = sel.css('.inner')

        # game_list = []
        for each in game_info:
            item = GameItem()
            name = each.css('h3 a::text').extract_first()
            rank = each.css('.rank::text').extract_first()
            rate = each.css('.fade::text').extract_first()

            item['name'] = name
            item['rank'] = rank
            item['rate'] = rate

            yield item

        if self.offset < 161:
            self.offset += 1
            yield scrapy.Request(self.baseUrl + str(self.offset), callback=self.parse, dont_filter=True)

# response.css('h3 a::text')[0].extract()
# response.css('.rank::text').extract_first()
# response.css('.fade::text').extract_first()
