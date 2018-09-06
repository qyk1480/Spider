import requests
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# url = 'https://www.baidu.com/s'
# kw = {'wd': '中国'}
# response = requests.get(url, params=kw, headers=headers)
# print(response.url)

url = "http://fanyi.youdao.com/translate"

key = input("输入内容：")
form = {
    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",

    "salt": "1531017090129",
    "sign": "d4f81c0f4209cc84e09ae160b678a736",

    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTION",
    "typoResult": "true",
}

response = requests.post(url, data=form, headers=headers)
html = response.content.decode()
result = json.loads(html)
print("结果是：%s" % (result["translateResult"][0][0]['tgt']))
