# from scrapy import cmdline
#
# if __name__ == "__main__":
#     # cmdline.execute("scrapy crawl get_sina_index -s JOBDIR=crawls/get_sina_index-1".split())
#     # cmdline.execute("scrapy crawl get_sina_index --logfile=crawls/get_sina_index.log".split())
#     while True:
#         cmdline.execute("scrapy crawl get_sina_index".split())
#         print(1)

# 引入你的爬虫
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
import time
import logging
from scrapy.utils.project import get_project_settings

# 在控制台打印日志
configure_logging()
# CrawlerRunner获取settings.py里的设置信息
runner = CrawlerRunner(get_project_settings())


@defer.inlineCallbacks
def crawl():
    while True:
        logging.info("new cycle starting")
        yield runner.crawl('get_sina_index')
        time.sleep(8)
    # reactor.stop()


crawl()
reactor.run()  # the script will block here until the last crawl call is finishe
