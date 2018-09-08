from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
# driver.maximize_window()

driver.get('http://127.0.0.1:5000/')
time.sleep(0.5)

nav_bar = ['Share', 'Home', 'Sign In']

index = 0
for x in nav_bar:
    if index < len(nav_bar):
        element = driver.find_element_by_link_text(x)
        index = index + 1
        print(x + ' is avaiable ----->OK')
        element.click()
        time.sleep(0.5)

ele_email = driver.find_element_by_id("email")
ele_email.send_keys("401316161@qq.com")
time.sleep(0.5)

ele_pwd = driver.find_element_by_id("password")
ele_pwd.send_keys("123")
time.sleep(0.5)

ele_submit = driver.find_element_by_id("submit")
ele_submit.click()
if driver.current_url == 'http://127.0.0.1:5000/':
    print(x + ' loggging successfully ----->OK')


'''
ele2 = driver.find_element_by_id("kw")
ele2.send_keys("SAMA")
time.sleep(0.5)
ele3 = driver.find_element_by_id("searchImg")
ele3.click()
time.sleep(0.5)
ele4 = driver.find_element_by_xpath("//table[@id='tzqc']/tbody/tr[2]/td[3]")

ele4.click()
ele5 = driver.find_element_by_link_text("原始数据")
time.sleep(0.5)
ele5.click()
'''
