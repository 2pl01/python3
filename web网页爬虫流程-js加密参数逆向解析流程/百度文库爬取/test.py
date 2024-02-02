# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： test.py
    @date：2023/12/19 16:29
    
"""
# -*- encoding=utf8 -*-
import os.path
from lxml import etree
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime

# 获取当前时间
now = datetime.datetime.now()

# 将当前时间格式化为字符串
timestamp = now.strftime("%Y%m%d%H%M%S")

def create_file(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
url="https://wenku.baidu.com/view/60a4b1a15bcfa1c7aa00b52acfc789eb162d9e98?aggId=undefined&fr=catalogMain_text_ernie_recall_v1%3Awk_recommend_main_graph&_wkts_=1704273809240"
resp=requests.get(url)
text = resp.text
html = etree.HTML(text)
img_list=html.xpath('//div[@class="mod flow-ppt-mod"]/div/div/img')
cnt =1

file_path= "./wendang"
create_file(file_path)
for i in img_list:
    try:
        img_url=i.xpath('./@src')[0]
    except:
        img_url=i.xpath('./@data-src')[0]
    file_name=f'{timestamp}page_{cnt}.jpg'
    print(file_name,img_url)
    resp=requests.get(img_url)
    # with open(file_name,'wb') as f:
    #     f.write(resp.content)
    with open(os.path.join(file_path, file_name), 'wb') as file:
        for chunk in resp.iter_content(chunk_size=8192):
            file.write(chunk)
    cnt += 1