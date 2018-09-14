from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('lang=zh_CN.UTF-8')
chrome_options.add_argument('user-agent="Mozilla/5.0"')
chrome_options.add_argument('--proxy-server=http://118.190.95.43:9001')
driver = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Google\Chrome\\Application\\chromedriver.exe', options=chrome_options)

url = 'http://httpbin.org/get?show_env=1'
driver.get(url)
driver.save_screenshot('1.png')
print(driver.page_source)
driver.quit()
