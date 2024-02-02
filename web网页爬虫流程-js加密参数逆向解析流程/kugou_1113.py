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

headers = {
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
cookies = {
    "kg_mid": "8462a9e79aaab05633c9bae2d5e9bf14",
    "kg_dfid": "3Mmwr41YwVms0FZ2VL08O2Ji",
    "kg_dfid_collect": "d41d8cd98f00b204e9800998ecf8427e",
    "Hm_lvt_aedee6983d4cfc62f509129360d6bb3d": "1698975885",
    "kg_mid_temp": "8462a9e79aaab05633c9bae2d5e9bf14",
    "Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d": "1699502301"
}
url = "https://complexsearch.kugou.com/v2/search/song"
params = {
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


# response = requests.get(url, headers=headers, params=params)
# print(response.text)

def get_time():
    # 获取当前时间戳（以毫秒为单位）
    # timestamp = datetime.datetime.now().timestamp() * 1000
    # 对时间戳进行四舍五入并取整
    timestamp = int(time.time() * 1000)
    # rounded_timestamp = int(round(timestamp))

    # print(timestamp)


def gen_md5(word):
    word = ''.join([x for x in word])
    encode_word = word.encode('utf-8')
    return hashlib.md5(encode_word).hexdigest()


url = "https://complexsearch.kugou.com/v2/search/song"


def guid():
    num = 1 + random.random()
    res = hex(int(65536 * num))[3:]
    return res


GUID = guid() + guid() + "-" + guid() + "-" + guid() + "-" + guid() + "-" + guid() + guid() + guid()


def gen_params(word):
    timestamp = int(time.time() * 1000)
    dfid = '-'  # dfid经过本人多次测试发现为-即可
    keyword = word
    mid = gen_md5(GUID)
    t = f'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014bitrate=0callback=callback123clienttime={timestamp}clientver=1000dfid={dfid}filter=10inputtype=0iscorrection=1isfuzzy=0keyword={keyword}mid={mid}page=1pagesize=30platform=WebFilterprivilege_filter=0srcappid=2919token=userid=0uuid={mid}NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'
    signature = gen_md5(t)
    params['clienttime'] = timestamp
    params['dfid'] = dfid
    params['keyword'] = keyword
    params['mid'] = mid
    params['uuid'] = mid
    params['signature'] = signature
    return params


response = requests.get(url, headers=headers, params=gen_params(input("请输入歌名或歌手: ")))

song_list_utf8 = json.loads(response.text[12:-2].encode('utf-8').decode('utf-8').encode('gbk', 'ignore').decode('gbk'))

song_list = song_list_utf8['data']['lists']


def get_Mp3_url():
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
    # t=f'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014clienttime=1700278822749clientver=20000dfid=11SKG21YwVcY0cGwvX4RyUdsencode_album_audio_id={MixSongID}mid={params["mid"]}platid=4srcappid=2919token=userid=0uuid={params["uuid"]}NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'
    # time = get_time()
    times = int(time.time() * 1000)
    t = f'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014clienttime={times}clientver=20000dfid=11SKG21YwVcY0cGwvX4RyUdsencode_album_audio_id={MixSongID}mid={params["mid"]}platid=4srcappid=2919token=userid=0uuid={params["uuid"]}NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'
    # 'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014clienttime={times}clientver=20000dfid=11SKG21YwVcY0cGwvX4RyUdsencode_album_audio_id={MixSongID}mid={params["mid"]}platid=4srcappid=2919token=userid=0uuid={params["uuid"]}NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'

    signature = gen_md5(t)
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
    # print(response.text)
    # exit()
    res_1 = json.loads(response.text)
    # print(res_1)
    # exit()
    return res_1['data']['play_url']


list_song = []
output = ''


def read_and_write(new_song):
    my_song='\n'.join(new_song)
    with open('PyQT5/DB/音乐.txt', 'w') as f:
        f.write(my_song)

for i, s in enumerate(song_list):
    num = s.get('Duration')
    Duration = math.trunc(num / 60)
    Duration2 = math.trunc(num % 60)
    # print("{}:{}".format(Duration1,Duration2))
    MixSongID = s.get("EMixSongID")
    # print(MixSongID)

    print(f'{"%02d" % (i + 1)}-----{s.get("FileName")}-----{"{}:{}".format("%02d" % Duration, Duration2)}-----{s.get("FileHash")}-----{MixSongID}----{get_Mp3_url()}')
    # print(f'{"%02d"%(i+1)}-----{s.get("FileName")}----{get_Mp3_url()}')
    # print(type(f'{"%02d"%(i+1)}'))
    # new_song ={"%02d"%(i+1)},{s.get("FileName")},{"{}:{}".format("%02d"%Duration,Duration2)},{s.get("FileHash")},{MixSongID},{get_Mp3_url()}
    #new_song = (f'{"%02d" % (i + 1)}-----{s.get("FileName")}-----{"{}:{}".format("%02d" % Duration, Duration2)}-----{s.get("FileHash")}-----{MixSongID}-----{get_Mp3_url()}')
    new_song = (f'{"%02d" % (i + 1)}-----{s.get("SongName")}-----{s.get("SingerName")}-----{s.get("AlbumName")}-----{MixSongID}-----{get_Mp3_url()}')
    #time.sleep(3)
    list_song.append(new_song)
    read_and_write(list_song)
    # list_song.insert('', i, values=(new_data))
    # new_data.update(new_song)
    # print(type(list_song))


# print(len(list_song))
# exit()
#

for item in list_song:
    output += str(item) + "\n"

print(output)

# def download():
#     while True:
#         inp_num=input("请输入你要下载的歌曲的序号:")
#         b=int(inp_num)-1
separator = '-----'
def split_string_by_different_length(data, separator):
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


def Sl_song():
    output = ''

    while True:
        num = input("请输入一个数字（输入 q 退出）：")
        if num == 'q':
            print("程序已退出。")
            break
        else:

            # num = int(input("请输入序号："))
            # 判断输入的序号是否在列表范围内
            num = int(num)
            if num >= 1 and num <= len(list_song):
                # 输出对应序号的字符串
                str_rong = list_song[num - 1]
                str_r = split_string_by_different_length(str_rong, separator)
                download(str_r[1], str_r[5])
            else:
                print("输入的序号超出范围！")
def download(sname, list):
    url = list
    sname = sname
    file_url = url
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
    Sl_song()
