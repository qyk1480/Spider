from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Google\Chrome\\Application\\chromedriver.exe', options=chrome_options)

driver.get("https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=")

with open("douban.html", 'w', encoding='utf-8') as f:
    f.write(driver.page_source)
time.sleep(3)
driver.save_screenshot('douban.png')

# 向下滚动10000像素
# js = "document.body.scrollTop=10000"
js = "var q=document.documentElement.scrollTop=10000"

driver.execute_script(js)
time.sleep(5)

driver.save_screenshot('douban2.png')

with open("douban2.html", 'w', encoding='utf-8') as f:
    f.write(driver.page_source)
driver.quit()
