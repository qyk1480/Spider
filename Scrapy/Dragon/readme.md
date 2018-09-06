http://blog.csdn.net/fly_yr/article/details/51540269


scrapy startproject dragon
cd dragon
scrapy genspider dragon "omic.dragonballcn.com"

scrapy crawl spider.name
scrapy shell "url"
respoense.body
respoense.headers
respoense.xpath('//title/text()').extract()

scrapy crawl law_spider -o items.json -t json