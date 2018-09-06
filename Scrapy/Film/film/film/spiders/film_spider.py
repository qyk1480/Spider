# -*- coding: utf-8 -*-
import scrapy

from film.items import FilmItem


class FilmSpider(scrapy.Spider):
    name = 'film_spider'
    allowed_domains = ['https://movie.douban.com/top250']
    offset = 0
    url = 'https://movie.douban.com/top250?start='
    start_urls = [url + str(offset), ]

    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//div[@class="info"]')
        # items = []
        for site in sites:
            item = FilmItem()
            item['title'] = site.xpath('div[@class="hd"]/a/span[@class="title"]/text()').extract()[0]
            item['star'] = site.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            item['desc'] = site.xpath('div[@class="bd"]/p/text()').extract()[0].strip()
            # items.append(item)

            yield item
        if self.offset < 225:
            self.offset += 25
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse, dont_filter=True)
