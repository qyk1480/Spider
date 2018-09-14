from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"')
driver = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Google\Chrome\\Application\\chromedriver.exe', options=chrome_options)

url = 'http://bangumi.tv/'
driver.get(url)
driver.save_screenshot('1.png')

newwindow = 'window.open("http://bangumi.tv/");'
cookies = {'name': 'qwe', 'value': '123'}
driver.delete_all_cookies()
driver.add_cookie(cookies)

driver.execute_script(newwindow)
driver.save_screenshot('2.png')
driver.quit()