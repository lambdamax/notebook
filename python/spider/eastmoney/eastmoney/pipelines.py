# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import requests
from .items import BaseSinaStock, BaseSinaFutures


class EastmoneyPipeline(object):
    def process_item(self, item, spider):
        print(item)
        return item


class SinaPipeline(object):
    def process_item(self, item, spider):
        csrftoken = spider.django_token
        if csrftoken:
            data = dict(item)
            data.update({'csrfmiddlewaretoken': csrftoken,
                         'title': isinstance(item, BaseSinaStock) and 'stock' or 'futures'})
            requests.post('http://localhost:5500/api/sinaspider', data=data, cookies=dict(csrftoken=csrftoken))
        return item
