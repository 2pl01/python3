# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： 文字识别.py
    @date：2024/01/04 16:53
    
"""
# encoding:utf-8
from pprint import pprint
import requests
import base64
import os
from docx import Document
import re
import json


# link = "https://wenku.baidu.com/view/d6b88ed8d0f34693daef5ef7ba0d4a7302766c99.html?fr=income2-doc-search&_wkts_=1704767875889&wkQuery=%E8%B6%A3%E5%91%B3%E7%AD%94%E9%A2%98%E5%8F%8A%E7%AD%94%E6%A1%88%E5%A4%A7%E5%85%A8%E5%90%88%E9%9B%86"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537'}
# html_data = requests.get(url=link, headers=headers).text
# print(html_data)
# print(re.findall('var pageData = (.*?);',html_data)[0])
# json_data = json.loads(re.findall('var pageData = (.*?);', html_data)[0])
# data = json_data["viewBiz"]["docInfo"]



# html_data = requests.get(url=link, headers=headers).content.decode('utf-8')
# print(html_data)
# json_data_1 = json.loads(re.findall('var pageData = (.*?);', html_data)[0])
# #
# #
# pprint(json_data_1)


# json_data=json_data_1['viewBiz']['docInfo']
# pprint(json_data_1['viewBiz']['docInfo'])
# json_data['title']

# for j in json_data_1['viewBiz']['docInfo']:
#     print(j)
#     name = j['title']  # 名字
#     score = j['score'] # 评分
#     viewCount = j['viewCount'] # 阅读量
#     downloadCount = j['downloadCount'] # 下载量
#     docId = j['docId'] # 数据包ID


# for j in json_data['wkSmallFlow']:
#     print(j('wkWeb4924'))
# def flatten_dict(d, parent_key='', result=None):
#     if result is None:
#         result = []
#     for k, v in d.items():
#         new_key = f"{parent_key}.{k}" if parent_key else k
#         if isinstance(v, dict):
#             flatten_dict(v, parent_key=new_key, result=result)
#         elif isinstance(v, list):
#             for item in v:
#                 result.append((new_key, item))
#         else:
#             result.append((new_key, v))
#     return result
#
#
# # 遍历嵌套字典和列表，并取出键和值存入列表中
# flattened_list = flatten_dict(json_data)
# for j in flattened_list:
#
#     print(f'{j.get("tetle")}')  # 名字
    # score = j['score'] # 评分
    # viewCount = j['viewCount'] # 阅读量
    # downloadCount = j['downloadCount'] # 下载量
    # docId = j['docId'] # 数据包ID

#print(flattened_list)

# def get_values(d):
#     values = []
#     for key, value in d.items():
#         if isinstance(value, dict):
#             values.extend(get_values(value))  # 递归调用函数处理嵌套字典的值
#         elif isinstance(value, list):
#             values.extend([item for item in value])  # 遍历列表中的元素并添加到values中
#         else:
#             values.append(value)  # 将值添加到values列表中
#     return values
#
# values = get_values(json_data)
# print(values)
#
#
# pprint(json_data)
# js=json.loads(json_data["viewBiz"]['docInfo'])
# pprint(type(js))
# for j in json_data['viewBiz']['docInfo'][0]:
#     name = j['title']  # 名字
    # score = j['score'] # 评分
    # viewCount = j['viewCount'] # 阅读量
    # downloadCount = j['downloadCount'] # 下载量
    # docId = j['docId'] # 数据包ID


# for item in json_data:
#     print("遍历字典...")
#     print("基础设施:")
#     infrastructure = item["infrastructure"]  # 获取基础设施字典
# def traverse_dict(json_data, level=0):
#     for key, value in json_data.items():
#         print("  " * level + str(key) + ":", end=" ")
#         if isinstance(value, dict):
#             print()
#             traverse_dict(value, level + 1)
#         else:
#             print(value)
# data = traverse_dict(json_data)
# print(type(data))

# for j in data:
#     print(j['title'])
# for key, value in json_data.items():  # 遍历基础设施字典的键和值
#     if key == "viewBiz":
#         print(f"{key}: {value}")  # 输出键和值的内容
#         for j in value.items():
#             print(j['title'])







    # print(f"")
    # print("docInfo")
    # for j in key['viewBiz']['docInfo']:
    #     print(j)





# for j in json_data['viewBiz']:
#
#     print(j)
    # name = j['title']  # 名字
    # score = j['score'] # 评分
    # viewCount = j['viewCount'] # 阅读量
    # downloadCount = j['downloadCount'] # 下载量
    # docId = j['docId'] # 数据包ID

#     print(j['title'])
    # print(type(j))
    # pprint(f"{value}")
# for j in json_data['viewBiz']['docInfo']:
#     name=j['tetle']
#     print(j['viewCount'])
# score =key['score']
# view=key['ViewCoun']
# downloadCount=key['downloadCoun']
# docId=key['showDocId']
# print(j[])


# 解析JSON数据





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


