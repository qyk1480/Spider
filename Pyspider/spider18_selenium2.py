import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import json


class douyuSelenium(unittest.TestCase):
    # 初始化方法
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Google\Chrome\\Application\\chromedriver.exe', options=chrome_options)
        self.file = open('douyu.json', 'w', encoding='utf-8')

    # 必须test开头
    def testDouyu(self):
        self.driver.get('https://www.douyu.com/directory/all')

        while True:
            # 指定xml解析
            soup = BeautifulSoup(self.driver.page_source, 'lxml')

            titles = soup.find_all('h3', {'class': 'ellipsis'})
            nums = soup.find_all('span', {'class': 'dy-num fr'})

            for title, num in zip(titles, nums):
                textstr = '观众人数：' + num.get_text().strip() + '\t房间标题：' + title.get_text().strip()
                print(textstr)
                jsontext = json.dumps(textstr, ensure_ascii=False) + '\n\n'
                self.file.write(jsontext)

            if self.driver.page_source.find('shark-pager-next shark-pager-disable shark-pager-disable-next') != -1:
                break

            self.driver.find_element_by_class_name('shark-pager-next').click()

    # 测试结束执行的方式
    def tearDown(self):
        print('加载完成')
        self.file.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
    # unittest.main(argv=['ignored', '-v'], exit=False)
