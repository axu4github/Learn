# coding=utf-8
from selenium import webdriver
import time

'''
爬虫爬取网页时，因为有时候有的网站使用selenium刷新完成后，不会显示所有商品；需要鼠标滚动才可以显示，所以需要自动滚动，以便获取所有商品。

示例：京东搜索页面 http://search.jd.com/Search?keyword=apple&enc=utf-8&stock=1&wtype=1&psort=3&page=1
等待刷新完成后，只刷新30条数据，但是第一页应该有60条数据。
（因为page=2默认被包含在page=1中，直接访问page=2的时候也会显示第一页的前30条，只有向下滚动的时候另外30条才会被ajax加载进来）
'''

url = 'http://search.jd.com/Search?keyword=apple&enc=utf-8&stock=1&wtype=1&psort=3&page=1'

driver = webdriver.Chrome()
try:
    driver.get(url)
    driver.implicitly_wait(10)  # 隐式等待10秒

    print "---- 刷新完成开始等待 ----"
    # 为突出效果，再等待5秒
    # time.sleep(10)
    print "---- 等待结束 ----"

    # 将页面滚动条拖到底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.implicitly_wait(10)  # 隐式等待10秒
    print "---- 滚动完成 ----"

    time.sleep(5)
except Exception, e:
    raise e
finally:
    driver.quit()
