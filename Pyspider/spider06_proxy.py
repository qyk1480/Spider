import urllib.request

proxyswitch = True
# 私密代理  环境变量
# authpproxy_handler = urllib.request.ProxyHandler({"http" : "name:pwd@180.97.193.58:3128"})

httpproxy_handler = urllib.request.ProxyHandler({"http": "180.97.193.58:3128"})
nullproxy_handler = urllib.request.ProxyHandler({})

if proxyswitch:
    opener = urllib.request.build_opener(httpproxy_handler)
else:
    opener = urllib.request.build_opener(nullproxy_handler())
# 全局opener,urlopen()也将使用定制的opener
urllib.request.install_opener(opener)

url = "http://www.baidu.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))
