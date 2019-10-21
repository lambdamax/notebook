# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals, http

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging import getLogger


class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        if spider.name == 'get_stock' and request.url == 'http://quote.eastmoney.com/center/gridlist.html#hs_a_board':
            driver = webdriver.Firefox()
            driver.get(request.url)
            WebDriverWait(driver, 100).until(
                EC.presence_of_element_located((By.ID, "table_wrapper-table"))
            )
            html = driver.page_source
            driver.quit()
            return http.HtmlResponse(url=request.url, body=html, request=request, encoding='utf-8')

    def spider_opened(self, spider):
        spider.logger.info('Eastmoney Spider opened: %s' % spider.name)
