# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BaseStock(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    code = scrapy.Field()
    link = scrapy.Field()


class BaseSinaStock(scrapy.Item):
    """
    股票类
    """
    name = scrapy.Field()
    price = scrapy.Field()
    rate = scrapy.Field()
    range = scrapy.Field()
    quantity = scrapy.Field()
    amount = scrapy.Field()


class BaseSinaFutures(scrapy.Item):
    """
    期货类
    """
    name = scrapy.Field()
    price = scrapy.Field()
    rate = scrapy.Field()
    range = scrapy.Field()
    last_price = scrapy.Field()
