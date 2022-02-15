from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.bcbxhome.com")
time.sleep(2)
print("编测编学网站已打开！")


