import scrapy
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class GetStock(scrapy.Spider):
    name = "get_stock"

    def start_requests(self):
        urls = [
            'http://quote.eastmoney.com/center/gridlist.html#hs_a_board',
        ]
        # driver = webdriver.Firefox()
        for url in urls:
            # driver.get(url)
            # WebDriverWait(driver, 100).until(driver.find_elements_by_id('Table0'))
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        print(response.body)
        driver = webdriver.Firefox()
        # driver.get(response.url)
        driver.get('http://quote.eastmoney.com/center/gridlist.html#hs_a_board')
        WebDriverWait(driver, 100).until(driver.find_elements_by_id('Table0'))


