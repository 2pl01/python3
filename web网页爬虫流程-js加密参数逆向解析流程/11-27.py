# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： kugou1109.py
    @date：2023/11/09 11:55

"""
import re

import requests
import random
import time
import hashlib
import json
import math
import datetime
import os


# 酷狗音乐主函数
class KuGoMusic():
    def __init__(self, url, input):
        self.word = input
        self.url = url
        # self.url = "https://complexsearch.kugou.com/v2/search/song"
        self.headers = {
            "authority": "complexsearch.kugou.com",
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "referer": "https://www.kugou.com/",
            "sec-ch-ua": "\"Microsoft Edge\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "script",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
        }

        self.params = {
            "callback": "callback123",
            "srcappid": "2919",
            "clientver": "1000",
            "clienttime": "",
            "mid": "",
            "uuid": "",
            "dfid": "",
            "keyword": "",
            "page": "1",
            "pagesize": "30",
            "bitrate": "0",
            "isfuzzy": "0",
            "inputtype": "0",
            "platform": "WebFilter",
            "userid": "0",
            "iscorrection": "1",
            "privilege_filter": "0",
            "filter": "10",
            "token": "",
            "appid": "1014",
            "signature": ""
        }
        # self.getData(self.url)

        # self.select_data(song_ling)

    def gen_md5(self, word):
        word = ''.join([x for x in word])
        encode_word = word.encode('utf-8')
        return hashlib.md5(encode_word).hexdigest()

    # 这个函数是为了
    def guid(self):
        num = 1 + random.random()
        res = hex(int(65536 * num))[3:]
        return res

    # GUID = guid() + guid() + "-" + guid() + "-" + guid() + "-" + guid() + "-" + guid() + guid() + guid()

    def gen_params(self, word):
        timestamp = int(time.time() * 1000)
        dfid = '-'  # dfid经过本人多次测试发现为-即可
        keyword = word
        GUID = self.guid() + self.guid() + "-" + self.guid() + "-" + self.guid() + "-" + self.guid() + "-" + self.guid() + self.guid() + self.guid()
        # print(GUID)
        mid = self.gen_md5(GUID)
        t = f'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014bitrate=0callback=callback123clienttime={timestamp}clientver=1000dfid={dfid}filter=10inputtype=0iscorrection=1isfuzzy=0keyword={keyword}mid={mid}page=1pagesize=30platform=WebFilterprivilege_filter=0srcappid=2919token=userid=0uuid={mid}NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'
        signature = self.gen_md5(t)
        self.params['clienttime'] = timestamp
        self.params['dfid'] = dfid
        self.params['keyword'] = keyword
        self.params['mid'] = mid
        self.params['uuid'] = mid
        self.params['signature'] = signature
        return self.params

    def getData(self, url):
        response = requests.get(url, headers=self.headers, params=self.gen_params(self.word))
        song_list_utf8 = json.loads(
            response.text[12:-2].encode('utf-8').decode('utf-8').encode('gbk', 'ignore').decode('gbk'))
        song_list = song_list_utf8['data']['lists']
        return song_list

    def select_data(self, song_ling):
        list_song = []
        for i, s in enumerate(song_ling):
            num = s.get('Duration')
            Duration = math.trunc(num / 60)
            Duration2 = math.trunc(num % 60)
            # print("{}:{}".format(Duration1,Duration2))
            MixSongID = s.get("EMixSongID")
            print(self.get_new_mp3(MixSongID))
            print(f'{"%02d" % (i + 1)}-----{s.get("FileName")}-----{"{}:{}".format("%02d" % Duration, Duration2)}-----{s.get("FileHash")}-----{MixSongID}')
            # print(f'{"%02d"%(i+1)}-----{s.get("FileName")}----{get_Mp3_url()}')-----{self.get_new_mp3(MixSongID)}-----{self.get_new_mp3(MixSongID)}
            # print(type(f'{"%02d"%(i+1)}'))
            # new_song ={"%02d"%(i+1)},{s.get("FileName")},{"{}:{}".format("%02d"%Duration,Duration2)},{s.get("FileHash")},{MixSongID},{get_Mp3_url()}
            new_song = (f'{"%02d" % (i + 1)}-----{s.get("FileName")}-----{"{}:{}".format("%02d" % Duration, Duration2)}-----{s.get("FileHash")}-----{MixSongID}')
            # time.sleep(1)
            list_song.append(new_song)

        return list_song
        # print(list_song)
        # self.get_new_mp3(MixSongID)

    def get_new_mp3(self, MixSongID):
        link = "https://wwwapi.kugou.com/play/songinfo"
        headers = {
            "authority": "wwwapi.kugou.com",
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "origin": "https://www.kugou.com",
            "referer": "https://www.kugou.com/",
            "sec-ch-ua": "\"Microsoft Edge\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
        }
        params = {
            "srcappid": "2919",
            "clientver": "20000",
            "clienttime": "1700645598516",
            "mid": "3b75aa785ba8051d0cc17c8a9b8698ce",
            "uuid": "3b75aa785ba8051d0cc17c8a9b8698ce",
            "dfid": "3MmxZV0fajI21CbUfv062nvb",
            "appid": "1014",
            "platid": "4",
            "encode_album_audio_id": "1uujyycb",
            "token": "",
            "userid": "0",
            "signature": "dc2ba2bc105459320e3d83e479c362f9\" --compressed -H \"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0\" -H \"Accept: */*\" -H \"Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2\" -H \"Accept-Encoding: gzip, deflate, br\" -H \"Origin: https://www.kugou.com\" -H \"Connection: keep-alive\" -H \"Referer: https://www.kugou.com/\" -H \"Sec-Fetch-Dest: empty\" -H \"Sec-Fetch-Mode: cors\" -H \"Sec-Fetch-Site: same-site\" -H \"TE: trailers\""
        }
        times = int(time.time() * 1000)
        t = f'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014clienttime={times}clientver=20000dfid=11SKG21YwVcY0cGwvX4RyUdsencode_album_audio_id={MixSongID}mid={params["mid"]}platid=4srcappid=2919token=userid=0uuid={params["uuid"]}NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'
        signature = self.gen_md5(t)
        data = {
            "srcappid": "2919",
            "clientver": "20000",
            "clienttime": times,
            "mid": params['mid'],
            "uuid": params['uuid'],
            "dfid": "11SKG21YwVcY0cGwvX4RyUds",
            "appid": "1014",
            "platid": "4",
            "encode_album_audio_id": MixSongID,
            "token": "",
            "userid": "0",
            "signature": signature
        }
        response = requests.get(url=link, headers=headers, params=data)
        res_1 = json.loads(response.text)
        return res_1['data']['play_url']

    separator = '-----'

    def split_string_by_different_length(self, data, separator):
        result = []
        start = 0
        while True:
            next_index = data.find(separator, start)
            if next_index == -1:
                result.append(data[start:])
                break
            else:
                result.append(data[start:next_index])
                start = next_index + len(separator)
        return result

    def my_input(self):  # 使用不同的名称来避免和内置函数的名字冲突
        num = input("请输入一个数字（输入 q 退出）：")
        # ... 其他代码

    def Sl_song(self, list_song, separator=None):
        output = ''
        while True:
            num = input("请输入一个数字（输入 q 退出）：")
            if num == 'q':
                print("程序已退出。")
                break
            else:
                num = int(num)
                if num >= 1 and num <= len(self.list_song):
                    str_rong = self.list_song[max(0, num - 1)]  # Ensure index is within the range of the list
                    str_r = self.split_string_by_different_length(str_rong, separator)
                    self.download(str_r[1], str_r[5])
                else:
                    print("输入的序号超出范围！")

    # def Sl_song(self, list_song, separator=None):
    #     output = ''
    #     while True:
    #         num = input("请输入一个数字（输入 q 退出）：")
    #         if num == 'q':
    #             print("程序已退出。")
    #             break
    #         else:
    #
    #             # num = int(input("请输入序号："))
    #             # 判断输入的序号是否在列表范围内
    #             num = int(num)
    #             if num >= 1 and num <= len(list_song):
    #                 # 输出对应序号的字符串
    #                 # print(type(output))
    #                 # exit()
    #                 str_rong = list_song[num - 1]
    #                 str_r = self.split_string_by_different_length(str_rong, separator)
    #                 # download(str_r[2],str_r[3],str_r[5])
    #                 # print(str_r)
    #                 self.download(str_r[1], str_r[5])
    #                 # return str_r[5]
    #
    #             else:
    #                 print("输入的序号超出范围！")

    def download(self, sname, list):
        url = list
        sname = sname
        file_url = url
        # = 'downloaded_file.mp3'
        current_path = os.getcwd()
        folder_path = "music"
        #
        # # 如果文件夹不存在，则创建文件夹
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        response = requests.get(file_url, stream=True)

        # os.path.join(folder_name, file_name)

        with open(os.path.join(folder_path, sname + '.mp3'), 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)


if __name__ == '__main__':
    input = input("请输入歌名或歌手: ")
    url = "https://complexsearch.kugou.com/v2/search/song"
    kugo = KuGoMusic(url, input)

    song_ling = kugo.getData(url)
    kugo.select_data(song_ling)
    # MixSongID=kugo.select_data(song_ling)
    # for i, s in enumerate(song_ling):
    #     num = s.get('Duration')
    #     Duration = math.trunc(num / 60)
    #     Duration2 = math.trunc(num % 60)
    #     MixSongID = s.get("EMixSongID")
    #     print(f'{"%02d" % (i + 1)}-----{s.get("FileName")}-----{"{}:{}".format("%02d" % Duration, Duration2)}-----{s.get("FileHash")}-----{MixSongID}-----{kugo.get_new_mp3(MixSongID)}')
    #     # print(f'{"%02d"%(i+1)}-----{s.get("FileName")}----{get_Mp3_url()}')-----{self.get_new_mp3(MixSongID)}-----{self.get_new_mp3(MixSongID)}
    #     # print(type(f'{"%02d"%(i+1)}'))
    #     # new_song ={"%02d"%(i+1)},{s.get("FileName")},{"{}:{}".format("%02d"%Duration,Duration2)},{s.get("FileHash")},{MixSongID},{get_Mp3_url()}
    #     #new_song = (f'{"%02d" % (i + 1)}-----{s.get("FileName")}-----{"{}:{}".format("%02d" % Duration, Duration2)}-----{s.get("FileHash")}-----{MixSongID}')
    #     # time.sleep(1)
    #     # list_song.append(new_song)

    # print(MixSongID)
    # exit()
