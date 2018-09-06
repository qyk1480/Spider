import scrapy

from dragon.items import DragonItem


class DragonSpider(scrapy.Spider):
    name = "dragon_spider"
    allowed_domains = ['comic.dragonballcn.com']
    start_urls = ['http://comic.dragonballcn.com/list/gain_1.php?did=0-0-0&fpp=10&fid=1']

    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('///form[@name="frmLinkContainer"]')
        items = []
        for site in sites:
            item = DragonItem()
            item['title'] = site.xpath('div/h2/text()').extract()
            item['link'] = site.xpath('input/@value').extract()
            items.append(item)

            yield item
        # return items

        # if not response.xpath('//li[@class="NavNextItem"]/a/@href').extract()[1] :
        url = response.xpath('//li[@class="NavNextItem"]/a/@href').extract()[1]

        yield scrapy.Request("http://comic.dragonballcn.com/list/" + str(url), callback=self.parse, dont_filter=True)


# response.xpath('//li[@class="NavNextItem"]/a/@href').extract()

# response.xpath('//form[@name="frmLinkContainer"]/div/h2/text()').extract()
# response.xpath('//form[@name="frmLinkContainer"]/input/@value').extract()
