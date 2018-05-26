from selenium import webdriver

path = "E:\\Git Repository\\python-tdd-book\\Chrome Web Driver\\chromedriver.exe"
browser = webdriver.Chrome(path)
browser.get('http://localhost:8000')

assert 'Django' in browser.title

