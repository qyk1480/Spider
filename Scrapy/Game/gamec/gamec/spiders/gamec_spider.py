# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from gamec.items import GamecItem


class GamecSpider(CrawlSpider):
    name = 'gamec_spider'
    allowed_domains = ['bangumi.tv']
    start_urls = ['http://bangumi.tv/game/browser/?sort=rank&page=1']

    pagelink = LinkExtractor(allow=('page=\d+'))
    print(pagelink)

    rules = (
        Rule(pagelink, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # sel = scrapy.selector.Selector(response)
        game_info = response.xpath('//ul[@class="browserFull"]/li/div[@class="inner"]')

        # game_list = []
        for each in game_info:
            item = GamecItem()
            name = each.xpath('./h3/a/text()').extract()[0]
            rank = each.xpath('./span[@class="rank"]/text()').extract()[0]
            rate = each.xpath('./p[@class="rateInfo"]/span/text()').extract()[0]

            item['name'] = name
            item['rank'] = rank
            item['rate'] = rate

            yield item
