import urllib.parse
import urllib.request


def tiebaSpider(url, page):
    for i in range(page):
        url = url + '&ie=utf-8&pn=' + str(i*50)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        html = response.read()

        filename = 'page' + str(i) + '.html'
        with open(filename, 'wb') as f:
            f.write(html)


def main():
    kw = input("输入贴吧名：")
    page = int(input("输入页数："))
    baseUrl = 'http://tieba.baidu.com/f?'
    kw = {'kw': kw}
    kw = urllib.parse.urlencode(kw)
    url = baseUrl + kw
    tiebaSpider(url, page)


if __name__ == '__main__':
    main()
