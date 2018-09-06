import urllib.request
from lxml import etree


class Spider:
    def __init__(self):
        pass

    def loadPage(self):
        url = 'https://tieba.baidu.com/p/5789852907?fid=11772&pid=120764072654&red_tag=0408308562#120764072654'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')

        xml = etree.HTML(html)
        link_list = xml.xpath('//img[@class="BDE_Image"]/@src')
        num = 0
        for link in link_list:
            num += 1
            self.saveImage(num, link)

    def saveImage(self, num, link):
        response = urllib.request.urlopen(link)
        html = response.read()
        name = str(num) + '.jpg'
        with open(name, 'wb') as f:
            f.write(html)


if __name__ == '__main__':
    spider = Spider()
    spider.loadPage()
