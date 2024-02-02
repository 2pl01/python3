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
# cookies = {
#     "kg_mid": "8462a9e79aaab05633c9bae2d5e9bf14",
#     "kg_dfid": "3Mmwr41YwVms0FZ2VL08O2Ji",
#     "kg_dfid_collect": "d41d8cd98f00b204e9800998ecf8427e",
#     "Hm_lvt_aedee6983d4cfc62f509129360d6bb3d": "1698975885",
#     "kg_mid_temp": "8462a9e79aaab05633c9bae2d5e9bf14",
#     "Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d": "1699502301"
# }
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
#response = requests.get(url, headers=headers, cookies=cookies, params=params)
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





response = requests.get(url, headers=headers, params=gen_params("稻香"))
# response = requests.get(url, headers=headers,  params=params)

# print(response.text)
FileHash_list = re.findall('"FileHash":"(.*?)"',response.text)
album_id_list=re.findall('"EMixSongID":"(.*?)"',response.text)
print(FileHash_list)
print(album_id_list)
song_list_utf8=json.loads(response.text[12:-2].encode('utf-8').decode('utf-8').encode('gbk', 'ignore').decode('gbk'))
#print(song_list_utf8)

song_list=song_list_utf8['data']['lists']

for i,s in enumerate(song_list):
    print(f'{i+1}-----{s.get("SongName")}-----{s.get("FileHash")}-----{s.get("EMixSongID")}')

# response = requests.get(url, headers=headers, params=gen_params(word)).text
# # response = requests.get(url, headers=headers,  params=params)
# print(response.text)
# print(response)