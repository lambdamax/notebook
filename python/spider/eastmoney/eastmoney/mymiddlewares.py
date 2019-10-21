# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from scrapy.http import HtmlResponse
from logging import getLogger


class SeleniumMiddleware(object):
    def __init__(self):
        self.logger = getLogger(__name__)
        self.driver = webdriver.Firefox()

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        if spider.name == 'get_stock':
            self.driver.get(request.url)
            WebDriverWait(self.driver, 100).until(
                self.driver.find_elements_by_id('Table0'))
            return HtmlResponse(url=request.url, body=self.driver.page_source, request=request, encoding='utf-8',
                                status=200)

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
