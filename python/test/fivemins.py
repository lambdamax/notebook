import requests
import re
import pandas as pd
import os
import time
import threading

gList = []
gCondition = threading.Condition()


# 连接API
def get_state(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Cache-Control': 'max-age=0',
        'Host': 'q.jrjimg.cn',
        'Upgrade-Insecure-Requests': '1'
    }
    r = requests.get(url, headers=headers)
    return r


# 分析response
def get_data(data, response):
    content = response.text
    # 整理格式
    content = re.sub(r'(\s|\n|\[|\")', '', content)
    content = re.sub(r'\],', '@@', content)
    # 数据时间
    clock = re.search(r'hqtime:([0-9]+)', content)
    clock = clock.groups()[0]
    # 全部涨幅数据
    regex = re.compile(r'HqData:(.*?)\]\]\}\;', re.S)
    result = regex.findall(content)[0].split('@@')
    data.append(['***', '***', '***', '***'])
    for i in result[:10]:
        row_need = []
        row = i.split(',')
        row_need.append([row[1], row[2], round((float(row[5]) - float(row[3])) * 100 / float(row[3]), 2), row[15]])
        data.extend(row_need)
    return data, clock


# 涨幅榜
class Up(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        while True:
            global gList
            global gCondition

            gCondition.acquire()
            while len(gList) > 0:
                gCondition.wait()
            resp = get_state(self.url)
            # 连接中断后等待
            if resp.status_code != 200:
                os.system('cls')
                gCondition.wait()
            get_data(gList, resp)
            gCondition.notify_all()
            gCondition.release()


# 跌幅榜
class Down(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        while True:
            global gList
            global gCondition

            gCondition.acquire()
            while len(gList) == 0:
                gCondition.wait()
            resp = get_state(self.url)
            if resp.status_code != 200:
                os.system('cls')
                gCondition.wait()
            data, clock = get_data(gList, resp)
            table = pd.DataFrame(data, columns=['Code', 'Name', 'Now%', '5m%'])
            print('data_time:' + clock)
            print(table)
            time.sleep(5)
            # 清空数据
            gList = []
            # 清屏
            os.system('cls')
            gCondition.notify_all()
            gCondition.release()


def run():
    url = 'http://q.jrjimg.cn/?q=cn|s|sa&c=s,ta,tm,sl,cot,cat,ape,min5pl&n=hqa&o=min5pl,%s&p=1020&_dc='
    Up(url % 'd').start()
    Down(url % 'a').start()


if __name__ == '__main__':
    run()
