from pyquery import PyQuery as pq
import requests
import os
from sys import stdout
import queue
import asyncio
import time


class QFJY:
    def __init__(self):
        self.url = "http://video.mobiletrain.org/course/index/courseId/548"
        self.path = None
        self.q = queue.Queue()
        self.urls = []
        self.check_save_path()
        self.workers = 0

    def check_save_path(self):
        base_path = "D:\download"
        dirname = "go2"
        self.path = os.path.join(base_path, dirname)
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def parse(self):
        req = requests.get(self.url)
        doc = pq(req.text)
        items = doc("div.course-list").items()
        for item in items:
            for a in item("a.fr").items():
                url = a.attr("data-url")
                self.urls.append(url)
                self.q.put(url)

    def download(self, url, filename):
        file_to_save = os.path.join(self.path, filename)
        with requests.get(url, stream=True) as r:
            filesize = r.headers["Content-Length"]
            total_size = int(filesize)
            print("下载文件基本信息:")
            print('-' * 30)
            print("文件名称:", filename)
            print("文件类型:", r.headers["Content-Type"])
            print("文件大小:", filesize, "bytes")
            print("下载地址:", url)
            print("保存路径:", file_to_save)
            print('-' * 30)
            if os.path.exists(file_to_save) and os.path.getsize(file_to_save) == total_size:
                print("检测到已存在")
                self.workers -= 1
                return
            print("开始下载")
            chunk_size = 128
            now_size = 0
            with open(file_to_save, 'wb') as f:
                for chunk in r.iter_content(chunk_size):
                    f.write(chunk)
                    # if now_size <= total_size:
                    #     stdout.write("下载进度: %.2f \r" % (now_size / total_size * 100))
                    #     now_size += chunk_size
                    # else:
                    #     stdout.write("结束下载")
                    #     print("下载完成")
        self.workers -= 1

    async def coroutine_download(self, url, filename):
        self.download(url, filename)

    def run(self):
        self.parse()
        for url in self.urls:
            filename = url.split('/')[-1]
            self.download(url, filename)

    async def run2(self):
        self.parse()
        while not self.q.empty():
            # if self.workers > 5:
            #     await asyncio.sleep(2)
            #     continue
            # url = self.q.get()
            # filename = url.split('/')[-1]
            self.workers += 1
            url1 = self.q.get()
            filename1 = url1.split('/')[-1]
            task1 = self.coroutine_download(url1, filename1)
            url2 = self.q.get()
            filename2 = url2.split('/')[-1]
            task2 = self.coroutine_download(url2, filename2)
            url3 = self.q.get()
            filename3 = url3.split('/')[-1]
            task3 = self.coroutine_download(url3, filename3)
            url4 = self.q.get()
            filename4 = url4.split('/')[-1]
            task4 = self.coroutine_download(url4, filename4)
            url5 = self.q.get()
            filename5 = url5.split('/')[-1]
            task5 = self.coroutine_download(url5, filename5)
            await asyncio.gather(
                task1,
                task2,
                task3,
                task4,
                task5
            )


if __name__ == "__main__":
    s = QFJY()
    now = time.time()
    # s.run()
    asyncio.run(s.run2())
    print(time.time() - now)
