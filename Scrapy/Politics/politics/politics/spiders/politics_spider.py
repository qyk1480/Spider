# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from politics.items import PoliticsItem


class PoliticsSpider(CrawlSpider):
    name = 'politics_spider'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/ruse?page=0']

    rules = (
        Rule(LinkExtractor(allow=r'index.php/question/questionType'), follow=True),
        Rule(LinkExtractor(allow=r'question/\d+/\d+.shtml'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'question/show\?id=\d+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        nodes = response.xpath('//div[@class="pagecenter p3"]')
        for node in nodes:
            item = PoliticsItem()
            title = response.xpath('.//strong[@class="tgray14"]/text()').extract()[0]
            print(title)
            num = title.split('\xa0')[2].split(':')[1]
            name = title.split('\xa0')[0].split('：')[1]
            content1 = response.xpath('.//div[@class="c1 text14_2"]/text()').extract()
            content2 = response.xpath('.//div[@class="contentext"]/text()').extract()
            content = content1 + content2
            url = response.url

            print(content)
            item['num'] = num
            item['name'] = name
            item['content'] = content
            item['url'] = url

            yield item

    # rules = (
    #     Rule(LinkExtractor(allow=r'index.php/question'), process_links='deal_links', follow=True),
    #     Rule(LinkExtractor(allow=r'question/\d+/\d+.shtml'), callback='parse_item', follow=False),

    # )

    # def deal_links(self, links):
    #     #Type&page=xxx?type=4 修改为 Type?page=xxx&type=4
    #     for link in links:
    #         link.url = link.url.replace('?', '&').replace('Type&', 'Type?')
    #     return links


# title = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
# num = title.split('\xa0')[2].split(':')[1]
# name = title.split('\xa0')[0].split('：')[1]
# content = response.xpath('//div[@class="pagecenter p3"]//div[@class="c1 text14_2"]/text()').extract()[0]
# content = response.xpath('//div[@class="pagecenter p3"]//div[@class="contentext"]/text()').extract()[0]
