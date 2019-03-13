#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_login.py
# @Author  : Ruanzhe
# @Date  : 2019/3/13  10:10


import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("http://ticketing-qa.ubtbus.top/#/login")
driver.maximize_window()
time.sleep(1)
username = driver.find_element_by_css_selector('input[sid="usernameInput"]')
username.send_keys("qa_ruanzhe")
password = driver.find_element_by_css_selector('input[sid="passwordInput"]')
password.send_keys("666666")
loginbutton = driver.find_element_by_css_selector('button[sid="loginBtn"]')
loginbutton.click()
time.sleep(3)
message = driver.find_element_by_css_selector('div[class="wel_title"] > i:first-child').text
print(message)
try:
	assert message == "Hi, qa_ruanzhe"
	print("Test Pass!")
except Exception as e:
	print("Test fail.", format(e))
finally:
	driver.quit()



