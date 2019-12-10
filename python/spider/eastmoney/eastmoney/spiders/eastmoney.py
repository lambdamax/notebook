import scrapy
from scrapy.selector import Selector
import re
from ..items import BaseStock


class GetStock(scrapy.Spider):
    name = "get_stock"

    def start_requests(self):
        urls = [
            # 'http://quote.eastmoney.com/center/gridlist.html#hs_a_board',
            "http://quote.eastmoney.com/stock_list.html"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        stock = BaseStock()
        se = Selector(response=response)
        lis = se.xpath('//*[@id="quotesearch"]/ul/li')
        for li in lis:
            cp = re.compile(r'(\w+).([6|0|3][0-9]{5}).')
            name = li.xpath('a/text()').extract()[0]
            link = li.xpath('a/@href').extract()[0]
            r = re.match(cp, name)
            if r:
                r = r.groups()
                stock['link'] = link
                stock['name'] = r[0]
                stock['code'] = r[1]
                yield stock

        # trs = se.xpath('//*[@id="table_wrapper-table"]/tbody/tr')
        # for tr in trs:
        #     stock['link'] = tr.xpath('td[2]/a/@href').extract()[0]
        #     stock['code'] = tr.xpath('td[2]/a/text()').extract()[0]
        #     stock['name'] = tr.xpath('td[3]/a/text()').extract()[0]
        #     yield stock
