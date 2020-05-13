# -*- coding: utf-8 -*-
import scrapy

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class EssilorSpider(scrapy.Spider):
    name = 'essilor'

    # allowed_domains = ['example.com']

    def __init__(self):
        self.browser = webdriver.Firefox()
        super().__init__()

    def start_requests(self):
        url = 'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-20537127107.84.424f37b0OcxzfP&id=528480381376&rn=dca8d1e404bf0e4e49c99e80c1bf24d2&abbucket=15&sku_properties=1626988:493262414'
        response = self.browser.get(url)
        self.browser.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys('222')
        self.browser.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys('222')
        yield response

    def parse(self, response):
        tab_comments = self.browser.find_element_by_xpath(
            '//*[@id="J_TabBar"]/li[2]/a')
        tab_comments.click()
        pass
