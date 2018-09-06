import urllib.request
import urllib.parse


url = 'http://dazi.kukuw.com/'
# 1
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
request = urllib.request.Request(url, headers=headers)
# 2
request = urllib.request.Request(url)
request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
# 3
baseUrl = 'http://www.baidu.com/'
keyword = input("输入：")
wd = {'wd': keyword}
wd = urllib.parse.urlencode(wd)
url = baseUrl + 's?' + wd
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
print(response.url)

response = urllib.request.urlopen(request)
html = response.read()
# print(html.decode())
print(request.get_header('User-agent'))
