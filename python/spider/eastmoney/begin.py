from scrapy import cmdline

if __name__ == "__main__":
    # cmdline.execute("scrapy crawl get_sina_index -s JOBDIR=crawls/get_sina_index-1".split())
    # cmdline.execute("scrapy crawl get_sina_index --logfile=crawls/get_sina_index.log".split())
    while True:
        cmdline.execute("scrapy crawl get_sina_index".split())
