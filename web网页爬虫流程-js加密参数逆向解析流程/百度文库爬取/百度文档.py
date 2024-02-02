# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： 百度文档.py
    @date：2024/01/04 15:37
    
"""
import requests
from docx import Document
import re
import json
from pprint import pprint
"""

获取数据，获取服务器返回响应数据2 .
开发者工具: response
response.json() 获取响应json字典数据，但是返回数据必须是完整json数据格式 花括号 
response.text 获取响应文本数据，返回字符串 任何时候都可以，但是基本获取网页源代码的时候
response.content 获取响应二进制数据，返回字节



"""
link="https://wenku.baidu.com/view/479bcc098ad63186bceb19e8b8f67c1cfbd6ee7a?aggId=d6b88ed8d0f34693daef5ef7ba0d4a7302766c99&_wkts_=1705030525724&wkQuery=%E8%B6%A3%E5%91%B3%E7%AD%94%E9%A2%98%E5%8F%8A%E7%AD%94%E6%A1%88%E5%A4%A7%E5%85%A8%E5%90%88%E9%9B%86"
#link="https://wenku.baidu.com/view/d6b88ed8d0f34693daef5ef7ba0d4a7302766c99.html?fr=income2-doc-search&_wkts_=1704767875889&wkQuery=%E8%B6%A3%E5%91%B3%E7%AD%94%E9%A2%98%E5%8F%8A%E7%AD%94%E6%A1%88%E5%A4%A7%E5%85%A8%E5%90%88%E9%9B%86"
headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537'}
html_data=requests.get(url=link,headers=headers)
print(type(html_data))
json_data=json.loads(re.findall('var pageData = (.*?);',html_data)[0])
#json_data=json_data_1['viewBiz']['docInfo']
pprint(json_data)

exit()
name=json_data['title']
score =json_data['viewBiz']['docInfo']['score']
view=json_data['viewBiz']['docInfo']['viewCount']
downloadCount=json_data['viewBiz']['docInfo']['downloadCount']
docId=json_data['viewBiz']['docInfo']['showDocId']
url="https://wenku.baidu.com/gsearch/rec/pcviewdocrec2023"
#url="https://wenku.baidu.com/view/479bcc098ad63186bceb19e8b8f67c1cfbd6ee7a?aggId=d6b88ed8d0f34693daef5ef7ba0d4a7302766c99&_wkts_=1705029364875&wkQuery=%E8%B6%A3%E5%91%B3%E7%AD%94%E9%A2%98%E5%8F%8A%E7%AD%94%E6%A1%88%E5%A4%A7%E5%85%A8%E5%90%88%E9%9B%86"
data={
"sessionId": "2741084368-2741084368",
"docId": docId,
"query": name,
"recPositions": "catalog,toplist"
}

headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537'}
responses=requests.get(url=url,params=data,headers=headers)
# print(responses.json())

num=1
# pprint(responses.json()['data']['catalogDoc'])
for index in responses.json()['data']['catalogDoc']:
    pic=index['pic']
    #pprint(pic)

    img_content=requests.get(url=pic,headers=headers).content
    with open('img\\'+str(num)+'.jpg',mode='wb')as f:
        f.write(img_content)
    print(pic)
    num +=1

