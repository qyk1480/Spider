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
        fkid = 'WC39ZUyXRgdGWzGOCElWoPMxDxSMGhEim5sBp0a6FvC1NbSD7TcF32qioI6JSgQX9+SMglT7ypSYR1s7UlXe2Hvk3/UCnkiaVP8oeLJ7ep4kBqkbBrqK/b1X5pVVE247je/Ysrz06apr8WQCkkJTqhEZ8pCNkGi2yQhzpvB+jhXggJ3fFAhs6WCPPSIoid/0hAD9XWhrlL37RqmQSKxxwV0qNp3IXhnVuuEH9alwqgXx1cvionFIHc04LQfvsOkAw1487577677129'
        yield scrapy.FormRequest.from_response(
            response,
            formdata = {
                        'gps': '',
                        'username': 'qyk1480',
                        'password': 'qykAIMIking13',
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