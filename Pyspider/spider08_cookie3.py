import urllib.request
from http import cookiejar

file = 'cookie.txt'
cookie = cookiejar.MozillaCookieJar()
cookie.load(file)
# 处理器对象
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(cookie_handler)

opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")]
# urllib.request.install_opener(opener)

get_url = 'http://bangumi.tv/'
response2 = opener.open(get_url)
print(response2.read().decode('utf-8'))
