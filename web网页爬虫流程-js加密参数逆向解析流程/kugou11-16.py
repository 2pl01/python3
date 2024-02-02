# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： kugou11-16.py
    @date：2023/11/16 15:33
    
"""
import requests
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


url='https://wwwapi.kugou.com/play/songinfo?srcappid=2919&clientver=20000&clienttime=1700121113878&mid=8462a9e79aaab05633c9bae2d5e9bf14&uuid=8462a9e79aaab05633c9bae2d5e9bf14&dfid=11SKG21YwVcY0cGwvX4RyUds&appid=1014&platid=4&encode_album_audio_id=4d25sx11&token=&userid=0&signature=96ac0278c055bb390920f353d811d550'
# url = "https://wwwapi.kugou.com/play/songinfo"
# params = {
#     "srcappid": "2919",
#     "clientver": "20000",
#     "clienttime": "1700120200991",
#     "mid": "bf4aa3f33999dd4981b7f53c9ea1979a",
#     "uuid": "bf4aa3f33999dd4981b7f53c9ea1979a",
#     "dfid": "11SKG21YwVcY0cGwvX4RyUds",
#     "appid": "1014",
#     "platid": "4",
#     "encode_album_audio_id": "j2sek95",
#     "token": "",
#     "userid": "0",
#     'signature': '4d16e76499b761bcd9378d5a47635fc6'
# }

res_1 = requests.get(url=url,headers=headers)

print(res_1.json())