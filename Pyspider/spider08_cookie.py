import urllib.parse
import urllib.request
from http import cookiejar
from bs4 import BeautifulSoup
import time

# http_handler = urllib.request.HTTPHandler()
# https_handler = urllib.request.HTTPSHandler()
# httpproxy_handler = urllib.request.ProxyHandler({"http": "121.43.235.100:90"})

cookie = cookiejar.CookieJar()
# 处理器对象
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(cookie_handler)
# opener = urllib.request.build_opener(http_handler, https_handler, httpproxy_handler, cookie_handler)
# http报头数据
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")]
# urllib.request.install_opener(opener)


url = 'http://bangumi.tv/login'
request = urllib.request.Request(url)
response = opener.open(request)
html = response.read()
soup = BeautifulSoup(html, 'lxml')
formhash = soup.find('input', attrs={'name': 'formhash'}).get('value')
print(formhash)

captchaUrl = 'http://bangumi.tv/signup/captcha?%d' % (time.time()*10000)
request = urllib.request.Request(captchaUrl)
response = opener.open(request)
with open('captcha.jpg', 'wb') as f:
    f.write(response.read())
text = input("输入验证码：")

# data = {"email":"1336726254@qq.com", "password":"qwebangumi123"}
data = {
    'formhash': formhash,
    'referer': 'http://bangumi.tv/',
    'dreferer': 'http://bangumi.tv/',
    'email': '1336726254@qq.com',
    'password': 'qwebangumi123',
    'captcha_challenge_field': text,
    'loginsubmit': '登录'
}
data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url, data=data)
response = opener.open(request)

get_url = 'http://bangumi.tv/'
response2 = opener.open(get_url)
print(response2.read().decode('utf-8'))

print(cookie)
# cookieStr = ""
# for item in cookie:
#     cookieStr = cookieStr + item.name + "=" + item.value + ";"

# 舍去最后一位的分号
# print(cookieStr[:-1])
