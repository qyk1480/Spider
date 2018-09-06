import urllib.request
import re


class Tspider:
    def __init__(self):
        pass

    def loadPage(self, div):
        url = 'https://tieba.baidu.com/p/532896930?see_lz=1&traceid=/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        # re.S 全文匹配
        p = re.compile(div, re.S)

        result = p.findall(html)
        self.dealPage(result)
        # for sth in result:
        #     print(sth)

    def dealPage(self, result):
        for sth in result:
            sth = sth.replace('<br>', '\n').replace('&gt;', '>')
            self.writePage(sth)

    def writePage(self, sth):
        with open('rem11.txt', 'a') as f:
            f.write(sth)

    def startWork(self):
        divlist = [
            '<div id="post_content_5394609862" class="d_post_content j_d_post_content ">(.*?)</div>',
            '<div id="post_content_5394609863" class="d_post_content j_d_post_content ">(.*?)</div>',
            '<div id="post_content_5394612253" class="d_post_content j_d_post_content ">(.*?)</div>',
            '<div id="post_content_5394612254" class="d_post_content j_d_post_content ">(.*?)</div>'
            ]

        for div in divlist:
            self.loadPage(div)


if __name__ == '__main__':
    spider = Tspider()
    spider.startWork()
