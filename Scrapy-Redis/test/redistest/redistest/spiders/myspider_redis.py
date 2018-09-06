from scrapy_redis.spiders import RedisSpider


class TestSpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'testspider_redis'
    redis_key = 'testspider:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(TestSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }
