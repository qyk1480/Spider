import requests

url = 'http://icanhazip.com/'
url2 = 'http://httpbin.org/ip'
url3 = 'http://httpbin.org/get?show_env=1'
url4 = 'https://www.ipip.net/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
proxies = {'http': 'http://118.190.95.43:9001'}
# proxies = {'https': 'http://106.75.226.36:808'}

response = requests.get(url, headers=headers, proxies=proxies)
html = response.text
print(html.strip())

