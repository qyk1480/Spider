from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import os
import redis
from hashlib import md5


class SimpleHash(object):
    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed

    def hash(self, value):
        ret = 0
        for i in range(len(value)):
            ret +=self.seed * ret + ord(value[i])
        return (self.cap - 1) & ret


class BloomFilter(object):
    def __init__(self, host='localhost', port=6379, db=0, blockNum=1, key='bloomfilter'):
        self.server = redis.StrictRedis(host=host, port=port, db=db)
        self.bit_size = 1 << 31
        self.seed = [5, 7, 11, 13, 31, 37, 61]
        self.key = key
        self.blockNum = blockNum
        self.hashfunc = []
        for seed in self.seed:
            self.hashfunc.append(SimpleHash(self.bit_size, seed))

    def isContains(self, str_input):
        if not str_input:
            return False
        m5 = md5()
        m5.update(str_input.encode('utf-8'))
        str_input = m5.hexdigest()
        ret = True
        name = self.key + str(int(str_input[0:2], 16) % self.blockNum)
        for f in self.hashfunc:
            loc = f.hash(str_input)
            ret = ret & self.server.getbit(name, loc)
        return ret

    def insert(self, str_input):
        m5 = md5()
        m5.update(str_input.encode('utf-8'))
        str_input = m5.hexdigest()
        name = self.key + str(int(str_input[0:2], 16) % self.blockNum)
        for f in self.hashfunc:
            loc = f.hash(str_input)
            self.server.setbit(name, loc, 1)


def get_html(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"')
    # chrome_options.add_argument('--proxy-server=http://118.190.95.43:9001')
    driver = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Google\Chrome\\Application\\chromedriver.exe', options=chrome_options)

    driver.get(url)
    js = "var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)
    # driver.save_screenshot('1.png')
    html = driver.page_source
    driver.quit()

    return html


def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    imgList = []
    img_list = soup.find('div', attrs={'class': 'post-img'}).find_all('p', attrs={'class': 'img-wp'})
    for img in img_list:
        imgaddr = img.find('img').get('src')
        imgList.append(imgaddr)
    print(imgList)
    return imgList


def deal_pict(imgurl):
    if not os.path.exists('D:\\Spider\\Exspider\\001_pict2redis\\OP'):
        os.mkdir('D:\\Spider\\Exspider\\001_pict2redis\\OP')
    os.chdir('D:\\Spider\\Exspider\\001_pict2redis\\OP')

    img = 'http://' + imgurl[2:]
    with open('11102' + img[-15:-9], 'wb') as f:
        image = requests.get(img, stream=True)
        for block in image.iter_content(1024):
            if not block:
                break
            f.write(block)


if __name__ == '__main__':
    url = 'http://hanhuazu.cc/cartoon/post?id=11102'
    # url = 'http://hanhuazu.cc/cartoon/post?id=11067'
    html = get_html(url)
    imgList = parse_html(html)

    for imgurl in imgList:
        bf = BloomFilter()
        if bf.isContains(imgurl):
            print('exists')
        else:
            print('not exists')
            bf.insert(imgurl)

            deal_pict(imgurl)
