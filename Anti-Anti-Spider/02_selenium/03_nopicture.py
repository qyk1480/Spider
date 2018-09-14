from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
prefs = {"profile.default_content_settings_values": {"images": 2}}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Google\Chrome\\Application\\chromedriver.exe', options=chrome_options)

url = 'https://www.baidu.com/'
driver.get(url)
driver.save_screenshot('3.png')
driver.quit()
