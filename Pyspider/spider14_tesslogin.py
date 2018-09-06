import requests
from bs4 import BeautifulSoup
import time

from pytesseract import image_to_string
from PIL import Image


def captcha(captcha_data):
    with open('captcha.jpg', 'wb') as f:
        f.write(captcha_data)
    time.sleep(3)
    # text = input("输入验证码：")
    # return text
    image = Image.open('captcha.jpg')
    text = image_to_string(image)
    print("机器识别的验证码为：" + text)
    command = input("Y:正确，其他自行输入：")
    if command.lower() == 'y':
        return text
    else:
        return input("captcha:")


def bangumiLogin():
    session = requests.session()

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    url = 'http://bangumi.tv/login'
    html = session.get(url, headers=headers).text

    bs = BeautifulSoup(html, 'lxml')

    formhash = bs.find('input', attrs={'name': 'formhash'}).get('value')
    print(formhash)
    captcha_url = 'http://bangumi.tv/signup/captcha?%d' % (time.time()*10000)
    captcha_data = session.get(captcha_url, headers=headers).content
    text = captcha(captcha_data)

    data = {
        'formhash': formhash,
        'referer': 'http://bangumi.tv/',
        'dreferer': 'http://bangumi.tv/',
        'email': '1336726254@qq.com',
        'password': 'qwebangumi123',
        'captcha_challenge_field': text,
        'loginsubmit': '登录'
    }

    post_url = 'http://bangumi.tv/FollowTheRabbit'
    response = session.post(post_url, data=data, headers=headers)

    print(response.content.decode())


if __name__ == "__main__":
    bangumiLogin()
