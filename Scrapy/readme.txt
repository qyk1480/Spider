1.Dragon 实现功能：
    dragon 下载图片
    idragon 使用ItemLoader,第二种方式下载图片

2.Film 实现功能：
    1.将数据存储到MongoDB中
    2.中间件添加User-Agent, Proxy

3.Game 实现功能：
    game:
        1.使用css而非xpath 提取数据
        2.尝试存储为.csv形式

    gamec:
        1.CrawlSpider

4.Json 实现功能：
    1.对json网页进行提取数据

5.Login 实现功能：
    1.使用cookie进行模拟登陆
    2.使用FormRequest进行模拟登陆(直接进行POST数据时使用)
    3.使用FormRequest.from_response进行模拟登陆

6.Politics 实现功能：
    1.CrawlSpider
    2.process_links

7.Sina 实现功能：
    1.多层级提取数据
    2. yield scrapy.Request(url, meta={'meta_2': item}, callback, dont_filter)
    3.Scrapy-Redis 基础
