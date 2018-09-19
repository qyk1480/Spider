# -*- coding: utf-8 -*-
import scrapy


class ShiSpider(scrapy.Spider):
    name = 'shi_spider'
    allowed_domains = ['www.shiyanlou.com']
    start_urls = ['https://www.shiyanlou.com/login?next=%2Fuser%2Faccount']

    def parse(self, response):
        form = {
            'login': 'xxxx',
            'password': 'xxxx',
            'next': '/user/account',
            'remember': ''
            }

        yield scrapy.FormRequest.from_response(
            response,
            formdata=form,
            callback=self.parse_page,
            # dont_filter = True
            )

    def parse_page(self, response):
        url = 'https://www.shiyanlou.com/'
        yield scrapy.Request(url, callback=self.parse_page2, dont_filter=True)

    def parse_page2(self, response):
        with open("qwe.html", "wb") as f:
            f.write(response.body)
