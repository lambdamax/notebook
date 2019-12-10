import scrapy
from scrapy.selector import Selector
from ..items import BaseStock


class GetStock(scrapy.Spider):
    name = "get_stock"

    def start_requests(self):
        urls = [
            'http://quote.eastmoney.com/center/gridlist.html#hs_a_board',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        stock = BaseStock()
        se = Selector(response=response)
        trs = se.xpath('//*[@id="table_wrapper-table"]/tbody/tr')
        for tr in trs:
            stock['link'] = tr.xpath('td[2]/a/@href').extract()[0]
            stock['code'] = tr.xpath('td[2]/a/text()').extract()[0]
            stock['name'] = tr.xpath('td[3]/a/text()').extract()[0]
            yield stock
