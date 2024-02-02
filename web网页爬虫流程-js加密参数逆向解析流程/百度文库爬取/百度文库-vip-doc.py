# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： 百度文库-vip-doc.py
    @date：2024/01/18 10:12
    
"""
import requests
import json
import pprint
import time
import random
import re
#url='https://wenku.baidu.com/ndocview/readerinfo?doc_id=f4786b906194dd88d0d233d4b14e852459fb3976&docId=f4786b906194dd88d0d233d4b14e852459fb3976&type=html&clientType=1&pn=3&t=1705651542834&isFromBdSearch=0&srcRef=&rn=50&powerId=2&bizName=mainPc&bdQuery=百度文库 "c": { "ix": 0, "iy": 0, "iw": 955, "ih": 1408 },如何解析'
#url="https://wenku.baidu.com/ndocview/readerinfo?doc_id=3d2e2a6883c758f5f61fb7360b4c2e3f5627252c&docId=3d2e2a6883c758f5f61fb7360b4c2e3f5627252c&type=html&clientType=100&pn=0&t=1705571524205&isFromBdSearch=0&srcRef=https%3A%2F%2Fwenku.baidu.com%2Fsearch&rn=100&powerId=2&bizName=mainPc&wkQuery=python%E9%A2%98%E5%BA%93"
url = "https://wenku.baidu.com/ndocview/readerinfo?doc_id=3d2e2a6883c758f5f61fb7360b4c2e3f5627252c&docId=3d2e2a6883c758f5f61fb7360b4c2e3f5627252c&type=html&clientType=1&pn=3&t=1705652221317&isFromBdSearch=0&srcRef=&rn=50&powerId=2&bizName=mainPc&wkQuery=python题库"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537'}

responses = requests.get(url=url, headers=headers)
print(responses)
responses.encoding="utf-8"
json_dict=responses.json()
# pattern = r'{.*?}'

page_list=json_dict["data"]["htmlUrls"]["json"]

print(page_list)

file=r"python题库.txt"
open(file,"w").close()
for index,page in enumerate(page_list,start=1):
    if index ==5:
        break
    page_url = page["pageLoadUrl"]
    try:
        time.sleep(random.randint(20,50)/20)
        resp=requests.get(page_url)
        data =resp.text.split("(",1)[1][:-1]
        json_data=json.loads(data)
        print(resp.text)
        pprint.pprint(json_data)
        for x in json_data["body"]:
            text = str(x["c"])

            #print(type(text))
            if type(text) is str:
                print(text)
                with open(file,"a",encoding="utf-8")as f:
                    f.write(text)
        print(f"download:{index}")
    except Exception as e:
        print(index,e)
        print("failed")


# pprint.pprint(json_dict)
#data = json.loads(re.findall('\{.*?.*\}', responses)[0])
# json_string = json.dumps(data)
#pprint.pprint(data)
# json_dict =json.loads()
# print(json_dict)


# print(responses)
