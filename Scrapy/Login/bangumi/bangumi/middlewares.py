# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from bangumi.settings import USER_AGENTS
from bangumi.settings import PROXIES
import base64

# from scrapy.downloadermiddlewares.redirect import RedirectMiddleware

# class ThreatDefenceRedirectMiddleware(RedirectMiddleware):
#     def _redirect(self, redirected, request, spider, reason):
#         # 如果没有特殊的防范性重定向那就正常工作
#         if not self.is_threat_defense_url(redirected.url):
#             return super()._redirect(redirected, request, spider, reason)

#         # logger.debug(f'Zipru threat defense triggered for {request.url}')
#         request.cookies = self.bypass_threat_defense(redirected.url)
#         request.dont_filter = True # 防止原始链接被标记为重复链接
#         return request

#     def is_threat_defense_url(self, url):
#         return '://zipru.to/threat_defense.php' in url


class RandomUserAgent(object):
    def process_request(self, request, spider):
        useragent = random.choice(USER_AGENTS)
        request.headers.setdefault('User-Agent', useragent)
        print(useragent)


class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        print(proxy)
        if proxy['user_passwd'] is None:
            request.meta['proxy'] = 'http://' + proxy['ip_port']


class BangumiSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
