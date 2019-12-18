import scrapy
from scrapy.selector import Selector
from ..items import *
import requests
from datetime import datetime


class SinaIndex(scrapy.Spider):
    name = "get_sina_index"

    def __init__(self):
        super().__init__()
        self.django_token = requests.get('http://localhost:5500/api/_get_token').text or None

    def start_requests(self):
        """
        名称，指数，涨跌，涨跌幅度，成交量（手），成交额（千万）
        var hq_str_s_sh000001="上证指数,2917.3157,2.8382,0.10,1701239,18061729";
        var hq_str_s_sz399001="深证成指,9915.87,39.598,0.40,259022858,28597966";
        var hq_str_s_sz399006="创业板指,1734.02,12.951,0.75,21326802,3603564";

        指数，，买价，卖价，最高价，最低价，时间，昨结算，开盘价，持仓量，买盘，卖盘，日期，名称
        var hq_str_hf_GC="1466.890,,1466.800,1466.900,1467.700,1464.200,15:49:44,1464.900,1466.300,497364.000,18,14,2019-12-10,纽约黄金";
        var hq_str_hf_OIL="64.188,,64.170,64.180,64.260,64.010,15:49:43,64.250,64.030,0.000,15,1,2019-12-10,布伦特原油";
        :return:
        """
        urls = []
        now_time = datetime.now()
        begin_time_str = now_time.strftime('%Y-%m-%d') + ' 9:29'
        end_time_str = now_time.strftime('%Y-%m-%d') + ' 15:01'
        begin_time = datetime.strptime(begin_time_str, '%Y-%m-%d %H:%M')
        end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M')

        if begin_time < now_time < end_time:
            urls.append(('stock', 'https://hq.sinajs.cn/rn=1575963644280&list=s_sh000001,s_sz399001,s_sz399006'))
        urls.append(('futures', 'https://hq.sinajs.cn/rn=1575963644280&list=hf_GC,hf_OIL'))
        for title, url in urls:
            yield scrapy.Request(url=url, callback=self.parse, cb_kwargs={'title': title})

    def parse(self, response, title):
        model = BaseSinaStock() if title == 'stock' else BaseSinaFutures()
        lines = response.text.split(';\n')[:-1]
        for line in lines:
            _, info = line.split('=')
            info = info[1:-1].split(',')
            if title == 'stock':
                model['name'] = info[0]
                model['price'] = float(info[1])
                model['range'] = float(info[2])
                model['rate'] = float(info[3])
                model['quantity'] = float(info[4])
                model['amount'] = float(info[5])
            else:
                model['name'] = info[-1]
                model['price'] = float(info[0])
            # print(model.name, model.price, model.rate, model.range, model.quantity, model.amount)
            yield model
