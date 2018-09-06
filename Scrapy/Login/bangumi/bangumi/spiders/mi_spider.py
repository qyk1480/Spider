# -*- coding: utf-8 -*-
import scrapy
import requests
import time


class MiSpider(scrapy.Spider):
    name = 'mi_spider'
    allowed_domains = ['bangumi.tv/']

    url = 'http://bangumi.tv/signup/captcha?%d' % (time.time()*10000)
    start_urls = [url]
    url2 = 'http://bangumi.tv/login'
    url3 = 'http://bangumi.tv/FollowTheRabbit'
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

    def start_requests(self):
        return [scrapy.Request(self.url, callback=self.parse2, dont_filter=True)]

    # def parse(self, response):
        # formhash = response.xpath('//form[@id="loginForm"]/input[@name="formhash"]/@value').extract()[0]
        # print(formhash)
        # captchaUrl = 'http://bangumi.tv/signup/captcha?%d' % (time.time()*10000)
        # return scrapy.Request(url, callback=self.parse2, dont_filter=True)

    def parse2(self, response):
        # formhash = response.meta['formhash']
        with open('captcha.jpg', 'wb') as f:
            f.write(response.body)
        text = input("输入验证码：")

        return scrapy.Request(self.url3, meta={'text': text}, callback=self.parse3, dont_filter=True)

    def parse3(self, response):
        formhash = response.xpath('//form[@id="loginForm"]/input[@name="formhash"]/@value').extract()[0]
        # formhash = response.meta['formhash']
        text = response.meta['text']
        form = {
                'formhash': formhash,
                'referer': 'http://bangumi.tv/',
                'dreferer': 'http://bangumi.tv/',
                'email': '1336726254@qq.com',
                'password': 'qwebangumi123',
                'captcha_challenge_field': text,
                'loginsubmit': '登录'
            }
        print(form)
        # time.sleep(5)
        yield scrapy.FormRequest.from_response(
            response,
            formdata=form,
            # meta = {'dont_redirect': True},
            # meta = {'cookiejar': response.meta['cookiejar'], 'dont_redirect': True},
            # headers = self.headers,
            callback=self.parse_page,
            dont_filter=True
            )
        # return scrapy.Request(self.url2, meta={'formhash': formhash, 'text': text}, callback=self.parse2, dont_filter=True)

    def parse_page(self, response):
        with open("qwe3.html", "wb") as f:
            f.write(response.body)
