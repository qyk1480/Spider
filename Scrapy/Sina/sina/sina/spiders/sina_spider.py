# -*- coding: utf-8 -*-
import scrapy
from sina.items import SinaItem
import os


class SinaSpider(scrapy.Spider):
    name = 'sina_spider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        items = []
        parentName = response.xpath('//div[@id="tab01"]//h3/a/text()').extract()
        parentUrl = response.xpath('//div[@id="tab01"]//h3/a/@href').extract()

        subName = response.xpath('//div[@id="tab01"]//h3/a/../..//ul[@class="list01"]/li/a/text()').extract()
        subUrl = response.xpath('//div[@id="tab01"]//h3/a/../..//ul[@class="list01"]/li/a/@href').extract()

        for i in range(len(parentName)):
            parentFile = os.curdir + os.sep + 'SinaData' + os.sep + parentName[i]
            if not os.path.exists(parentFile):
                os.makedirs(parentFile)

            for j in range(len(subName)):
                item = SinaItem()

                item['parentName'] = parentName[i]
                item['parentUrl'] = parentUrl[i]

                if subUrl[j].startswith(item['parentUrl']):
                    subFile = parentFile + os.sep + subName[j]
                    if not os.path.exists(subFile):
                        os.makedirs(subFile)

                    item['subName'] = subName[j]
                    item['subUrl'] = subUrl[j]
                    item['subFile'] = subFile

                    items.append(item)

        for item in items:
            yield scrapy.Request(url=item['subUrl'], meta={'meta_1': item}, callback=self.parse_two, dont_filter=True)

    def parse_two(self, response):
        meta_1 = response.meta['meta_1']

        contentUrl = response.xpath('//a/@href').extract()

        items = []
        for i in range(len(contentUrl)):
            # if (contentUrl[i].startswith(meta_1['parentUrl']) and contentUrl[i].endswith('.shtml')):
            if contentUrl[i].endswith('.shtml'):
                item = SinaItem()
                item['parentName'] = meta_1['parentName']
                item['parentUrl'] = meta_1['parentUrl']
                item['subName'] = meta_1['subName']
                item['subUrl'] = meta_1['subUrl']
                item['subFile'] = meta_1['subFile']
                item['contentUrl'] = contentUrl[i]
                items.append(item)

        for item in items:
            yield scrapy.Request(url=item['contentUrl'], meta={'meta_2': item}, callback=self.parse_three, dont_filter=True)

    def parse_three(self, response):
        item = response.meta['meta_2']
        content = ''
        title = response.xpath('//h1[@class="main-title"]/text()').extract()
        title2 = response.xpath('//h1[@id="artibodyTitle"]/text()').extract()
        title3 = response.xpath('//h1[@id="main_title"]/text()').extract()
        title.extend(title2)
        title.extend(title3)

        content_list = response.xpath('//div[@class="article"]/p/text()').extract()
        content_list2 = response.xpath('//div[@class="article"]/div/p/text()').extract()
        content_list3 = response.xpath('//div[@id="artibody"]/p/text()').extract()
        content_list.extend(content_list2)
        content_list.extend(content_list3)

        for cont in content_list:
            content += (cont + '\n')

        item['title'] = title
        item['content'] = content

        yield item
