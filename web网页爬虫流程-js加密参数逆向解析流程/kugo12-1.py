# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： kugo12-1.py
    @date：2023/12/01 15:21
    
"""

import requests
import random
import time
import hashlib
import json
import math
import datetime
import os
import re
import prettytable as pt


def search_md5(world,date_time):
    search_s=[
        "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt",
        "appid=1014",
        "bitrate=0",
        "callback=callback123",
        f"clienttime={date_time}",
        "clientver=1000",
        "dfid=11SKG21YwVcY0cGwvX4RyUds",
        "filter=10",
        "inputtype=0",
        "iscorrection=1",
        "isfuzzy=0",
        f"keyword={world}",
        "mid=8462a9e79aaab05633c9bae2d5e9bf14",
        "page=1",
        "pagesize=30",
        "platform=WebFilter",
        "privilege_filter=0",
        "srcappid=2919",
        "token=",
        "userid=0",
        "uuid=8462a9e79aaab05633c9bae2d5e9bf14",
        "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
    ]
    search_string = ''.join(search_s)
    MD5 = hashlib.md5()
    MD5.update(search_string.encode('utf-8'))
    search_signature = MD5.hexdigest()
    return search_signature


def Hash_md(audio_id,date_time):

    s=["NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt","appid=1014",
        #时间戳
        f"clienttime={date_time}","clientver=20000","dfid=11SKG21YwVcY0cGwvX4RyUds",
        #歌曲ID
        f"encode_album_audio_id={audio_id}", "mid=8462a9e79aaab05633c9bae2d5e9bf14",
        "platid=4","srcappid=2919",
        "token=",
        "userid=0",
        "uuid=8462a9e79aaab05633c9bae2d5e9bf14",
        "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
    ]
    string=''.join(s)
    MD5=hashlib.md5()
    MD5.update(string.encode('utf-8'))
    signature=MD5.hexdigest()
    return signature
# audio_id='4lstd758'
date_time = int(time.time() * 1000)
signature = Hash_md(audio_id,date_time)
# print(signature)
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

search_url ='https://complexsearch.kugou.com/v2/search/song'
while True:
    date_time = int(time.time() * 1000)
    key=input("请输入您要下载的歌曲或歌手名:")
    if key=='00':
        break
    search_signature = search_md5(key,date_time)
    search_data = {
        "callback": "callback123",
        "srcappid": "2919",
        "clientver": "1000",
        "clienttime": date_time,
        "mid": "8462a9e79aaab05633c9bae2d5e9bf14",
        "uuid": "8462a9e79aaab05633c9bae2d5e9bf14",
        "dfid": "11SKG21YwVcY0cGwvX4RyUds",
        "keyword": key,
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
        "signature": search_signature
    }




    response=requests.get(url=search_url,params=search_data,headers=headers)
    search_data=response.text
    html=re.findall('callback123\((.*)',search_data)[0].replace(')','')
    search_json_data=json.loads(html)
    # print(search_json_data)
    tb = pt.PrettyTable()
    tb.field_names = [
            '序号',
            '戨名',
            '戨手',
            '专辑',
            '歌曲ID',
    ]
    num=0
    lis=[]
    for index in search_json_data['data']['lists']:
        dit={
            '戨名':index['SongName'],
            '戨手':index['SingerName'],
            '专辑':index['AlbumName'],
            '歌曲ID':index['EMixSongID'],
        }
        lis.append(dit)
        tb.add_row([num,index['SongName'],index['SingerName'],index['AlbumName'],index['EMixSongID']])
        num += 1

    print(tb)
    page=input('请输入你要下载的歌曲序号:')
    audio_id =lis[int(page)]['歌曲ID']
    signature = Hash_md(audio_id,date_time)

    url = "https://wwwapi.kugou.com/play/songinfo"
    params = {
        "srcappid": "2919",
        "clientver": "20000",
        "clienttime": date_time,
        "mid": "8462a9e79aaab05633c9bae2d5e9bf14",
        "uuid": "8462a9e79aaab05633c9bae2d5e9bf14",
        "dfid": "11SKG21YwVcY0cGwvX4RyUds",
        "appid": "1014",
        "platid": "4",
        "encode_album_audio_id": audio_id,
        "token": "",
        "userid": "0",
        "signature": signature
    }
    response = requests.get(url, headers=headers, params=params)
    json_data = response.json()
    print(response.text)
    print(response)

    audio_name=json_data['data']['audio_name']
    pyay_url=json_data['data']['play_url']


    music_content = requests.get(url=pyay_url,headers=headers).content
    with open('music\\'+audio_name+'.mp3',mode='wb') as f:
        f.write(music_content)
        print(audio_name,pyay_url)

