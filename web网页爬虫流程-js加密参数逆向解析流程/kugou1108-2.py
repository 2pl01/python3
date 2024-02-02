# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： kugou1108-2.py
    @date：2023/11/08 12:09
    
"""
import json
import asyncio
import requests
import execjs
from hashlib import md5
import time
import threading


# 酷狗音乐主函数
class KuGoMusic():
    def __init__(self, input):
        self.new_md5 = md5()
        self.url = "https://complexsearch.kugou.com/v2/search/song"
        self.headers = {
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
        }
        mid = self.get_mid()
        self.child_url = "https://wwwapi.kugou.com/yy/index.php?r=play/getdata&mid={}".format(mid)
        self.query = ""
        self.params = ["NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt", "appid=1014", "bitrate=0", "callback=callback123",
                       "clienttime={}".format(int(time.time() * 1000)), "clientver=1000",
                       "dfid=4XSQkz1mmSGI2XV1Ud1xgR9V", "filter=10", "inputtype=0", "iscorrection=1", "isfuzzy=0",
                       "keyword={}".format(input), "mid={}".format(mid), "page=1", "pagesize=30", "platform=WebFilter",
                       "privilege_filter=0",
                       "srcappid=2919", "token=", "userid=0", "uuid={}".format(mid),
                       "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"]
        self.info = "".join(self.params)
        self.new_md5.update(self.info.encode(encoding='utf-8'))
        self.signature = self.new_md5.hexdigest()
        del self.params[0]
        del self.params[-1]
        self.params.append("signature={}".format(self.signature))

    def get_mid(self):
        with open('getBaseInfo.min.js', 'r', encoding='utf-8') as f:
            text = f.read()
        js_data = execjs.compile(text)
        mid = js_data.call('get_mid')
        return mid

        # 保存音频给你们当练习写(我没写 = =)
        def with_open(self, url):
            pass

    def get_query(self):
        # self.params.__iter__()
        for index, item in enumerate(self.params):
            if len(self.params) - 1 <= index:
                self.query += item
                break
            self.query += "{}&".format(item)

    def getData(self, url):
        res = requests.get(url, headers=self.headers).json()
        print(res['data']['audio_name'], res['data']['play_url'], res['data']['album_name'])

    async def getData2(self, url):
        loop = asyncio.get_event_loop()
        # requests模块默认不支持异步操作，所以就使用线程池来配合实现了。
        future = await loop.run_in_executor(None, requests.get, url, self.headers)
        res = future.json()
        print(res['data']['audio_name'], res['data']['play_url'], res['data']['album_name'])

    def getData_Threads(self, lists):
        threads = []

        for row in lists:
            url_child = self.child_url + "&album_audio_id={}".format(row["ID"])
            threads.append(threading.Thread(target=self.getData, args=(url_child,)))

        for thread in threads:
            # 执行
            thread.start()
        for thread in threads:
            # 结束
            thread.join()

    def getData_test(self, lists):
        for row in lists:
            url_child = self.child_url + "&album_audio_id={}".format(row["ID"])
            self.getData(url_child)

    def getData_async(self, lists):
        tasks = []
        for row in lists:
            url_child = self.child_url + "&album_audio_id={}".format(row["ID"])
            tasks.append(self.getData2(url_child))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))

    def parse_text(self, text):
        lists = json.loads(text)['data']['lists']
        # 多线程
        # self.getData_Threads(lists)
        # 普通
        # self.getData_test(lists)
        # 协程
        self.getData_async(lists)

    def run(self):
        self.get_query()
        url = "{0}?{1}".format(self.url, self.query)
        res = requests.get(url, headers=self.headers)
        self.parse_text(res.text[12:-2])


if __name__ == '__main__':
    input = input("请输入歌名或歌手: ")
    kugo = KuGoMusic(input)
    kugo.run()
