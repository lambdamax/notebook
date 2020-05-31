import requests
from pyquery import PyQuery as pq
from elasticsearch import Elasticsearch
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class Spider:
    def __init__(self):
        self.es = Elasticsearch(['172.29.21.169'], http_auth=('elastic', 'elastic'), port=9200)
        self.urls = [
            'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-20537127107.59.6e4737b00XxGPW&id=528480381376&rn=fe3c44d45f7efa16ec90c0da65a31ee5&abbucket=10&sku_properties=1626988:493262414',
        ]
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)

    def parse(self):
        page = self.driver.page_source
        doc = pq(page)
        items = doc('#J_Reviews div.tm-rate-content .tm-rate-fulltxt').items()
        for item in items:
            print(item.text())
            self.put_into_es(dict(comment=item.text()))

    def put_into_es(self, data: dict):
        self.es.index(index="essilor_product_comments", body=data)

    def run(self):
        self.parse()


if __name__ == '__main__':
    s = Spider()
