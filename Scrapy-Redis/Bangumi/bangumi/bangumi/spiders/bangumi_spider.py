# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bangumi.items import BangumiItem


class BangumiSpider(CrawlSpider):
    name = 'bangumi_spider'
    allowed_domains = ['bangumi.tv']
    start_urls = ['http://bangumi.tv/game/browser?sort=rank']

    pagelink = LinkExtractor(allow=('page=\d+'))
    infolink = LinkExtractor(allow=('subject/\d+'))

    rules = (
        Rule(pagelink, follow=True),
        Rule(infolink, callback='parse_item')
    )

    def parse_item(self, response):
        item = BangumiItem()
        item['name'] = self.getname(response)
        item['name_ch'] = self.getname_ch(response)
        item['rank'] = self.getrank(response)
        item['score'] = self.getscore(response)
        item['info'] = self.getinfo(response)

        yield item

    def getname(self, response):
        name = response.xpath('//div[@class="wrapperNeue"]//h1[@class="nameSingle"]/a/text()').extract()
        if len(name):
            name = name[0]
        else:
            name = 'null'
        return name

    def getname_ch(self, response):
        name_ch = response.xpath('//div[@class="wrapperNeue"]//ul[@id="infobox"]/li[1]/text()').extract()
        if len(name_ch):
            name_ch = name_ch[0]
        else:
            name_ch = 'null'
        return name_ch

    def getrank(self, response):
        rank = response.xpath('//div[@class="wrapperNeue"]//div[@class="global_score"]/div/small[@class="alarm"]/text()').extract()
        if len(rank):
            rank = rank
        else:
            rank = 'null'
        return rank

    def getscore(self, response):
        score = response.xpath('//div[@class="wrapperNeue"]//div[@class="global_score"]/span/text()').extract()
        if len(score):
            score = score
        else:
            score = 'null'
        return score

    def getinfo(self, response):
        info = response.xpath('//div[@class="wrapperNeue"]//div[@class="ll"]/div/text()').extract()
        if len(info):
            info = info
        else:
            info = 'null'
        return info
