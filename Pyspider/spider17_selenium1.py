from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

# driver = webdriver.PhantomJS(executable_path=r"D:\\Spiderware\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Google\Chrome\\Application\\chromedriver.exe', options=chrome_options)

driver.get("http://bangumi.tv/login")

driver.find_element_by_name("email").send_keys("1336726254@qq.com")
driver.find_element_by_id("password").send_keys("qwebangumi123")
driver.find_element_by_xpath('//input[@class="inputBtn"]').click()
time.sleep(3)
driver.save_screenshot("bangumi1.png")
text = input('验证码：')
driver.find_element_by_id("captcha").send_keys(text)
driver.find_element_by_xpath('//input[@class="inputBtn"]').click()

# time.sleep(3)
driver.save_screenshot("bangumi2.png")

ac1 = driver.find_element_by_xpath('//a[@class="top chl"]/span')
ActionChains(driver).move_to_element(ac1).perform()
time.sleep(2)
driver.save_screenshot("bangumi3.png")
ActionChains(driver).click(ac1).perform()
time.sleep(2)
driver.save_screenshot("bangumi4.png")

# with open("bangumi.html", 'w') as f:
#     f.write(driver.page_source)


driver.quit()
