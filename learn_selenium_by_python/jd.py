# -*- coding: utf-8 -*- 

'''
=== 用于京东抢卷 ===
需设置京东用户名和密码，执行后死循环（每次循环默认等待5秒）

'''

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import base64

urls = [
    "https://coupon.jd.com/ilink/couponSendFront/send_index.action?key=0e9aa90450224a9dbd0228966de08194&roleId=3049334&to=sale.jd.com/act/cwr5bu6ftg.html&",
]
sleepTime = 5 # 等待时间
username = "" # 京东账号
password = "" # 京东密码
driver = webdriver.Chrome()

try:
    while True:
        for url in urls:
            driver.get(url)
            try:
                driver.find_element_by_id("loginname").send_keys(username)
                driver.find_element_by_id("nloginpwd").send_keys(base64.b64decode(password))
                driver.find_element_by_id("loginsubmit").click()
                # 等待登陆后的页面刷新
                time.sleep(sleepTime)
            # 已经登陆
            except NoSuchElementException, e: time.sleep(sleepTime)

finally:
    driver.close()
