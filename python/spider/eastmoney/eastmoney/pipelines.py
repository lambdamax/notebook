# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import requests


class EastmoneyPipeline(object):
    def process_item(self, item, spider):
        print(item)
        return item


class SinaPipeline(object):
    def process_item(self, item, spider):
        # print(dict(item))
        data = dict(item).update({'csrfmiddlewaretoken': spider.django_token})
        requests.post('http://localhost:5500/blog/sinaspider', data=data)
        return item
