from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
#driver.maximize_window()

driver.get('http://www.cnblogs.com/yoyoketang/')
ele1 = driver.page_source

print(ele1)