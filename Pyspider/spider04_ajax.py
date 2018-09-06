import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action='
formdata = {
    'start': '0',
    'limit': '20',
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
data = urllib.parse.urlencode(formdata).encode('utf-8')

request = urllib.request.Request(url, data=data, headers=headers)
response = urllib.request.urlopen(request)

html = response.read().decode('utf-8')

print(html)

# https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=
