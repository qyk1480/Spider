import requests
from bs4 import BeautifulSoup
import time


def login():
    session = requests.session()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

    get_url = 'http://bangumi.tv/login'
    html = session.get(get_url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    formhash = soup.find('input', attrs={'name': 'formhash'}).get('value')
    print(formhash)
    # %d 自动省略小数
    captchaUrl = 'http://bangumi.tv/signup/captcha?%d' % (time.time()*10000)
    response = session.get(captchaUrl, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(response.content)
    text = input("输入验证码：")

    data = {
        'formhash': formhash,
        # 'referer': 'http://bangumi.tv/',
        # 'dreferer': 'http://bangumi.tv/',
        'email': '1336726254@qq.com',
        'password': 'qwebangumi123',
        'captcha_challenge_field': text,
        'loginsubmit': '登录'
    }
    post_url = 'http://bangumi.tv/FollowTheRabbit'
    response = session.post(post_url, data=data, headers=headers)
    print(response.content.decode())


if __name__ == '__main__':
    login()

# bs.find("input", attrs={"name":"_xsrf"}).get("value")
