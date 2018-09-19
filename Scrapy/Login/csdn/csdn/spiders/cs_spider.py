# -*- coding: utf-8 -*-
import scrapy


class CsSpider(scrapy.Spider):
    name = 'cs_spider'
    allowed_domains = ['csdn.net']
    start_urls = ['https://passport.csdn.net/account/login']

    def parse(self, response):
        lt = response.xpath('//div[@class="user-pass"]//input[@name="lt"]/@value').extract()
        execution = response.xpath('//div[@class="user-pass"]//input[@name="execution"]/@value').extract()
        # fkid = response.xpath('//div[@class="user-pass"]//input[@name="fkid"]/@value').extract()
        fkid = 'xxxx'
        yield scrapy.FormRequest.from_response(
            response,
            formdata = {
                        'gps': '',
                        'username': 'xxxx',
                        'password': 'xxxx',
                        'rememberMe': 'true',
                        'lt': lt,
                        'execution': execution,
                        'fkid': fkid,
                        '_eventId': 'submit',
            },
            callback = self.parse_page
            )

    def parse_page(self, response):
        with open('qwe.html', 'wb') as f:
            f.write(response.body)