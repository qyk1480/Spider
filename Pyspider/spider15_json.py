import urllib.request
import json
import jsonpath

url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)

html = response.read()

unicodestr = json.loads(html)

citylist = jsonpath.jsonpath(unicodestr, "$..name")
codelist = jsonpath.jsonpath(unicodestr, "$..code")

file = open('city.json', 'w')
for city, code in zip(citylist, codelist):
    array = json.dumps(city + '  ' + code, ensure_ascii=False)
    file.write(array + '\n')
file.close()
