import urllib.request

http_handler = urllib.request.HTTPHandler(debuglevel=1)
# https_handler = urllib.request.HTTPSHandler()

opener = urllib.request.build_opener(http_handler)

url = "http://www.baidu.com/"
request = urllib.request.Request(url)

response = opener.open(request)
# print(response.read())
