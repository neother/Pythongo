from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://cctvtzqc.com/rank')
ele1 = driver.find_element_by_link_text("中量组")
ele1.click()
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
