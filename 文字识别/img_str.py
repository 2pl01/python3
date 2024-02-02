# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： img_str.py
    @date：2024/01/31 11:21
    
"""
import pprint

from aip import AipOcr
from 文字识别 import dome
config={
    'appId': '46392424',
    'apiKey': 'wza8bUAxjcVDO3HhIxSkSN61',
    'secretKey': 'mp84ltRVLGfSIEp3sORVktKnHsjPSkqG'
}
client = AipOcr(**config)

def get_file_content(file):
    with open(file,'rb') as f:
        return f.read()

#把图片里的文字识别出来
def img_to_str(image_path):
    image=get_file_content(image_path)
    res= client.handwriting(image)
    #pprint.pprint(res)
    if 'words_result' in  res:
        return '\n'.join([w['words'] for w in res['words_result']])


res = img_to_str(r'D:\1-26.jpg')
print(res)