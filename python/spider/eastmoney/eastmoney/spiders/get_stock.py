import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GetStock(scrapy.Spider):
    name = "get_stock"

    def start_requests(self):
        urls = [
            'http://quote.eastmoney.com/center/gridlist.html#hs_a_board',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # self.driver.get(self.cur_url)
        # WebDriverWait(self.driver, 100).until(
        #     EC.presence_of_element_located((By.ID, "table_wrapper-table"))
        # )
        # driver.get(response.url)
        print(response.body)


