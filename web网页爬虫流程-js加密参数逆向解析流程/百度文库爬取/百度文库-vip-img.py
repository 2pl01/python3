# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： 百度文库-vip-img.py
    @date：2024/01/19 16:32
    
"""
import requests
import json
import pprint
import time
import random
import re
import base64
import os
from docx import Document
#获取url
url="https://wenku.baidu.com/ndocview/readerinfo?doc_id=3d2e2a6883c758f5f61fb7360b4c2e3f5627252c&docId=3d2e2a6883c758f5f61fb7360b4c2e3f5627252c&type=html&clientType=100&pn=0&t=1705891551707&isFromBdSearch=0&srcRef=https:%2F%2Fwenku.baidu.com%2Fsearch&rn=50&powerId=2&bizName=mainPc&wkQuery=python%E9%A2%98%E5%BA%93"
#url = "https://wenku.baidu.com/ndocview/readerinfo?doc_id=3d2e2a6883c758f5f61fb7360b4c2e3f5627252c&docId=3d2e2a6883c758f5f61fb7360b4c2e3f5627252c&type=html&clientType=1&pn=0&t=1705652221317&isFromBdSearch=0&srcRef=&rn=100&powerId=2&bizName=mainPc&wkQuery=python题库"
#请求
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537'}
#请求
responses = requests.get(url=url, headers=headers)
#设置编码
responses.encoding = "utf-8"
json_dict = responses.json()
page_list = json_dict["data"]["htmlUrls"]["png"]
file = 'img\\'

num=0
for index, page in enumerate(page_list, start=1):

    page_url = page["pageLoadUrl"]

    time.sleep(random.randint(20, 50) / 20)


    img_content = requests.get(url=page_url, headers=headers).content
    with open('img\\' + str(num) + '.jpg', mode='wb') as f:
        f.write(img_content)
    print(page_url)
    num += 1
def get_content(file):
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=wza8bUAxjcVDO3HhIxSkSN61&client_secret=mp84ltRVLGfSIEp3sORVktKnHsjPSkqG'
    response = requests.get(host)
    access_token = response.json()['access_token']


    '''
    通用文字识别（高精度版）
    '''

    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    # 二进制方式打开图片文件
    f = open(file, 'rb')
    img = base64.b64encode(f.read())
    params = {"image":img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    json_data = requests.post(request_url, data=params, headers=headers).json()
    words= '\n'.join([i['words'] for i in json_data['words_result']])
    return words
content_list=[]
files = os.listdir('img\\')
for file in files:
    filename='img\\'+file
    words = get_content(file=filename)
    print(words)
    content_list.append(words)
doc =Document()
content='\n'.join(content_list)
doc.add_paragraph(content)
doc.save('data.docx')