import requests
from bs4 import BeautifulSoup
import time


session = requests.session()

get_url = 'http://bangumi.tv/login'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

html = session.get(get_url, headers=headers).text
soup = BeautifulSoup(html, 'lxml')
formhash = soup.find('input', attrs={'name': 'formhash'}).get('value')

captchaUrl = 'http://bangumi.tv/signup/captcha?%d' % (time.time()*10000)
response = session.get(captchaUrl, headers=headers)
with open('captcha.jpg', 'wb') as f:
    f.write(response.content)
text = input("输入验证码：")

# form中的name
data = {
    'formhash': formhash,
    'referer': 'http://bangumi.tv/',
    'dreferer': 'http://bangumi.tv/',
    'email': 'xxxx',
    'password': 'xxxx',
    'captcha_challenge_field': text,
    'loginsubmit': '登录'
}

# 使用session请求登录后的页面
post_url = "http://bangumi.tv/FollowTheRabbit"
response = session.post(post_url, headers=headers, data=data)
# response = session.get(url, headers=headers)

with open('1.html', 'w', encoding='utf-8') as f:
    f.write(response.content.decode())

# cookie = "key:value,"
# cookie_dict = {i.split("=")[0]:i.split("=")[1] for i in cookie.split(";")}
