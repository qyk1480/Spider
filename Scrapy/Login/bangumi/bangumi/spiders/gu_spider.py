# -*- coding: utf-8 -*-
import scrapy
import json


# 一开始就发送POST请求，不调用start_urls
# 只需要post数据，不需要获取其他条件时使用
class GuSpider(scrapy.Spider):
    name = 'gu_spider'
    allowed_domains = ["bangumi.tv/"]
    start_urls = ["http://bangumi.tv/"]

    def start_requests(self):
        url = "http://fanyi.youdao.com/translate"
        key = input("输入内容：")
        form = {
            "i": key,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",

            "salt": "1531017090129",
            "sign": "d4f81c0f4209cc84e09ae160b678a736",

            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_CLICKBUTTION",
            "typoResult": "true",
        }
        yield scrapy.FormRequest(
            url=url,
            formdata=form,
            callback=self.parse_page)

    def parse_page(self, response):
        with open('qwe2.html', 'wb') as f:
            f.write(response.body)
        html = response.body.decode('utf-8')
        result = json.loads(html)
        print("结果是：%s" % (result["translateResult"][0][0]['tgt']))
