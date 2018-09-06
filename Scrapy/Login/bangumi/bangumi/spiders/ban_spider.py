# -*- coding: utf-8 -*-
import scrapy


class BanSpider(scrapy.Spider):
    name = 'ban_spider'
    allowed_domains = ['bangumi.tv/']
    start_urls = ['http://bangumi.tv/']

    cookie = 'chii_cookietime=0; chii_auth=4xKCm2%2BgJm8dNCCDZfJ3aoIzZvR0Ki72DUpMqM37oUnPt7RhhwroeE2c%2BQBVnHSqjUsG4qdii%2FJWYWkIfq3oYVNEpoBTNJJx5mO7; chii_sid=KPZZ2U'
    cookies = {i.split('=')[0]: i.split('=')[1] for i in cookie.split(';')}

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url, cookies=self.cookies, callback=self.parse_page)

    def parse_page(self, response):
        with open('qwe.html', 'wb') as f:
            f.write(response.body)

    # def parse(self, response):
    #     with open('qwe.html', 'wb') as f:
    #         f.write(response.body)
