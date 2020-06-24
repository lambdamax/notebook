from pyquery import PyQuery as pq
import requests
import os
from sys import stdout
import time


class QFJY:
    def __init__(self):
        self.url = "http://video.mobiletrain.org/course/index/courseId/548"
        self.path = None
        self.urls = []
        self.check_save_path()
        self.chunk_size = 128

    def check_save_path(self):
        base_path = "D:\download"
        # base_path = "C:\Afiles"
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

    def download(self, url, filename):
        file_to_save = os.path.join(self.path, filename)
        with requests.get(url, stream=True) as resp:
            filesize = resp.headers["Content-Length"]
            total_size = int(filesize)
            print("下载文件基本信息:")
            print('-' * 30)
            print("文件名称:", filename)
            print("文件类型:", resp.headers["Content-Type"])
            print("文件大小:", filesize, "bytes")
            print("下载地址:", url)
            print("保存路径:", file_to_save)
            print('-' * 30)
            if os.path.exists(file_to_save) and os.path.getsize(file_to_save) == total_size:
                print("检测到已存在")
                return
            print("开始下载")
            now_size = 0
            with open(file_to_save, 'wb') as f:
                for chunk in resp.iter_content(self.chunk_size):
                    f.write(chunk)
                    if now_size <= total_size:
                        stdout.write("下载进度: %.2f \r" % (now_size / total_size * 100))
                        now_size += self.chunk_size
                    else:
                        stdout.write("结束下载")
                        print("下载完成")

    def run(self):
        self.parse()
        for url in self.urls:
            filename = url.split('/')[-1]
            self.download(url, filename)


if __name__ == "__main__":
    now_time = time.time()
    s = QFJY()
    s.run()
    print(time.time() - now_time)
