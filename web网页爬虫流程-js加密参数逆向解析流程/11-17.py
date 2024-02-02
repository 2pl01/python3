# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： 11-17.py
    @date：2023/11/17 11:35
    
"""
# import requests
#
#
# headers = {
#     "authority": "wwwapi.kugou.com",
#     "accept": "*/*",
#     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#     "origin": "https://www.kugou.com",
#     "referer": "https://www.kugou.com/",
#     "sec-ch-ua": "\"Microsoft Edge\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-site",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
# }
# url = "https://wwwapi.kugou.com/play/songinfo"
# params = {
#     "srcappid": "2919",
#     "clientver": "20000",
#     "clienttime": "1700192063722",
#     "mid": "8462a9e79aaab05633c9bae2d5e9bf14",
#     "uuid": "8462a9e79aaab05633c9bae2d5e9bf14",
#     "dfid": "11SKG21YwVcY0cGwvX4RyUds",
#     "appid": "1014",
#     "platid": "4",
#     "encode_album_audio_id": "j2sek95",
#     "token": "",
#     "userid": "0",
#     "signature": "bf0fa952710524afd454bb19f3bb8de3"
# }
# response = requests.get(url, headers=headers, params=params)
#
# print(response.text.encode('utf-8').decode('utf-8').encode('gbk', 'ignore').decode('gbk'))
# print(response)

import requests


# headers = {
#     "authority": "fxsong3.kugou.com",
#     "accept": "*/*",
#     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#     "if-modified-since": "Fri, 17 Nov 2023 03:58:41 GMT",
#     "referer": "https://www.kugou.com/",
#     "sec-ch-ua": "\"Microsoft Edge\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "script",
#     "sec-fetch-mode": "no-cors",
#     "sec-fetch-site": "same-site",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
# }
# cookies = {
#     "kg_mid": "8462a9e79aaab05633c9bae2d5e9bf14",
#     "kg_dfid": "11SKG21YwVcY0cGwvX4RyUds",
#     "Hm_lvt_aedee6983d4cfc62f509129360d6bb3d": "1698975885",
#     "kg_dfid_collect": "d41d8cd98f00b204e9800998ecf8427e",
#     "kg_mid_temp": "8462a9e79aaab05633c9bae2d5e9bf14",
#     "Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d": "1700193461"
# }
# url = "https://fxsong3.kugou.com/fxmusic/pcad/lrcV1"
# params = {
#     "jsonCallBack": "",
#     "songName": "稻香 (女声版)",
#     "callback": "jsonphttpsfxsong3kugoucomfxmusicpcadlrcV1jsonCallBacksongNameE7A8BBE9A69920E5A5B3E5A3B0E78988callback"
# }
# response = requests.get(url, headers=headers, cookies=cookies, params=params)
#
# print(response.text)
# print(response)
import requests


headers = {
    "authority": "wwwapi.kugou.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://www.kugou.com",
    "pragma": "no-cache",
    "referer": "https://www.kugou.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
url = "https://wwwapi.kugou.com/play/songinfo"
params = {
    "srcappid": "2919",
    "clientver": "20000",
    "clienttime": "1700207876300",
    "mid": "93496844ccb7830073d08eca7cf9503b",
    "uuid": "93496844ccb7830073d08eca7cf9503b",
    "dfid": "0jHhKj0iduqI37p1J13hYaVC",
    "appid": "1014",
    "platid": "4",
    "encode_album_audio_id": "4d25sx11",
    "token": "",
    "userid": "0",
    "signature": "d372b863ed8ae53d74d0d8407f19d8c0"
}
response = requests.get(url, headers=headers, params=params)

print(response.json())
print(response)