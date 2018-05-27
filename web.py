from selenium import webdriver
import time

ie_driver = "E:\\Git Repository\\python-tdd-book\\Internet Explorer Web Driver\\IEDriverServer.exe"

browser = webdriver.Ie(ie_driver)
browser.get("http://127.0.0.1:8000/")
browser.set_window_size(1024,768)

time.sleep(1)

inputbox = browser.find_element_by_id('id_new_item')
print(inputbox.location['x'])
print(inputbox.size['width'])

browser.quit()
