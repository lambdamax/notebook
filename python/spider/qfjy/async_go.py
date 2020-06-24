from pyquery import PyQuery as pq
import requests
import os
from sys import stdout
import queue
import asyncio
import time
import aiohttp
import logging

_logger = logging.getLogger(__name__)


class QFJY:
    def __init__(self):
        self.url = "http://video.mobiletrain.org/course/index/courseId/548"
        self.path = None
        self.q = queue.Queue()
        self.check_save_path()
        self.workers = 10
        self.chunk_size = 128

    def info(self, filename, filetype, size, url, path):
        _logger.warning('-' * 30)
        msg = ['文件名称:{filename}',
               '文件类型:{filetype}',
               '文件大小:{size}bytes',
               '下载地址:{url}',
               '保存路径:{path}']
        _logger.warning("\n".join(msg).format(filename=filename, filetype=filetype, size=size, url=url, path=path))
        _logger.warning('-' * 30)

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
                self.q.put(url)

    async def download(self, url, filename):
        file_to_save = os.path.join(self.path, filename)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                filesize = resp.headers["Content-Length"]
                total_size = int(filesize)
                self.info(filename, resp.headers["Content-Type"], filesize, url, file_to_save)
                if os.path.exists(file_to_save) and os.path.getsize(file_to_save) == total_size:
                    _logger.warning(filename + "检测到已存在")
                    return
                with open(file_to_save, 'wb') as f:
                    async for content in resp.content.iter_chunked(self.chunk_size):
                        f.write(content)

    async def run(self):
        self.parse()
        urls = []
        while not self.q.empty():
            if len(urls) < self.workers:
                url = self.q.get()
                urls.append(url)
                if not self.q.empty():
                    continue
            tasks = [asyncio.create_task(self.download(url, url.split('/')[-1])) for url in urls]
            await asyncio.gather(*tasks)
            urls.clear()

    async def test1(self):
        await asyncio.sleep(2)
        print("test1")

    async def test2(self):
        await asyncio.sleep(2)
        print("test2")

    async def test_run(self):
        task1 = asyncio.create_task(self.test1())
        task2 = asyncio.create_task(self.test2())
        await asyncio.gather(task1, task2)

        # await self.test1()
        # await self.test2()


if __name__ == "__main__":
    now_time = time.time()
    s = QFJY()
    # asyncio.run(s.test_run())
    asyncio.run(s.run())
    print(time.time() - now_time)
