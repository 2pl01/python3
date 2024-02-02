# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： 雨伞.py
    @date：2024/01/22 11:48
    @爬取10086商城
"""
import json
import pprint

import requests
from selenium import webdriver
key =input("请输入关键字:")
url = "https://jf.10086.cn/cmcc-web-shop/search/query"
#头部文件要写全：主机名 Content-Type User-Agent origin Referer
headers = {
    "authority":"jf.10086.cn",
    "path":"/cmcc-web-shop/search/quer",
    "Content-Type":"application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "origin": "https://jf.10086.cn",
    " ":"https://jf.10086.cn/"
}
# josn_data={"sortColumn": "default", "sortType": "DESC", "pageSize": 60, "pageNum": 1, "kindName": key,
#      "kindList": "[{\'kindName\':\'key\',\'kindLevel\':\'small\'}]", "integral": 'null', "province": 'null'}

josn_data={"sortColumn":"default","sortType":"DESC","pageSize":60,"pageNum":1,"kindName":key,"kindList":"[{\"kindName""\":\"整理收纳\",\"kindLevel\":\"small\"},{\"kindName\":\"集优汇家居日用品\",\"kindLevel\":\"small\"}]","integral":"null","province":"null"}


print(josn_data["kindList"])


response = requests.post(url=url,json=josn_data,headers=headers)
json_dict = response.json()
pprint.pprint(json_dict)
# print(response.json())

