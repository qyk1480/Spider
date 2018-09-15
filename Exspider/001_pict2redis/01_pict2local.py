from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import os


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


def deal_pict(imgList):
    if not os.path.exists('./OP'):
        os.mkdir('./OP')
    os.chdir('./OP')
    for img in imgList:
        img = 'http://' + img[2:]
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
    deal_pict(imgList)
