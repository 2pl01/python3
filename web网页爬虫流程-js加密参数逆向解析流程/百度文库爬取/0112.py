# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： 0112.py
    @date：2024/01/12 9:48
    
"""
# import json
# import os
# import re
# from urllib.request import urlretrieve
#
# import requests
#
#
# class BaiduWk:
#     def __init__(self):
#         self.list_info = []
#         self.session = requests.session()
#         self.headers = {
#             'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 \
#             (KHTML, like Gecko) Chrome/80.0.3987.87 Mobile Safari/537.36'}
#
#     # 获取网页源代码的数据
#     def get_html(self, start_url):
#         response = self.session.get(start_url, headers=self.headers)
#         response.encoding = response.apparent_encoding
#         return response.text
#
#     # 获取文档标题, 提取请求参数
#     def parse_html(self, data):
#         re_title = re.findall("'title': '(.*?)',", data)
#         title = re_title[0] if re_title else re.findall('<title>(.*?)</title>', data)[0]
#         params = {
#             'bucketNum': re.findall(r'"bucketNum":(\d+)', data)[0],
#             'md5sum': re.findall('md5sum=(.*?)&', data)[0],
#             'sign': re.findall('sign=(.*?)&', data)[0],
#             'rtcs_flag': re.findall('rtcs_flag=(.*?)&', data)[0],
#             'rtcs_ver': re.findall('rtcs_ver=(.*?)&', data)[0],
#             'rsign': re.findall('"rsign":"(.*?)"', data)[0], }
#         # 提取页码列表
#         page_range = re.findall(r'{"page":\d+,"range":"(.*?)"}', data)
#         return params, page_range, title
#
#     # 以页码列表依次迭代
#     def words_data(self, params, page_range):
#         pages = len(page_range) + 1
#         url = r'https://wkrtcs.bdimg.com/rtcs/webapp'
#         for i in range(1, pages):
#             print(f'正在解析第{i}页数据，飞速读取中...')
#             # 添加所需的页码信息
#             params['pn'] = i
#             params['range'] = page_range[i - 1]
#             response = self.session.get(url, params=params).text
#             yield response
#
#     # 解析文章数据
#     def get_words(self, response):
#         pages = 1
#         for data in response:
#             # 转化为json数据
#             a = data[5:-1]
#             text = ''
#             d = json.loads(a)
#             # 提取 c键 的文本数据
#             for j in d['document.xml']:
#                 for c in j['c']:
#                     text += '\n'
#                     for c2 in c['c']:
#                         try:
#                             text += c2['c'] + '\n'
#                         except:
#                             continue
#             text += f'\n------------------------当前第{pages}页-------------------------\n'
#             pages += 1
#             self.list_info.append(text)
#
#     # 保存文件
#     def save_info(self, title, path):
#         os.makedirs('百度文库', exist_ok=True)
#         with open(path, 'w', encoding='utf-8') as f:
#             f.writelines(self.list_info)
#
#     def get_img(self, start_url):
#         print('开始尝试解析百度文库图片...\n')
#         r = self.session.get(start_url)
#         r.encoding = r.apparent_encoding
#         title = re.findall("'title': '(.*?)'", r.text)[0]
#         print(title)
#         docId = re.findall("'docId': '(.*?)'", r.text)[0]
#         totalPageNum = re.findall("'totalPageNum': '(.*?)'", r.text)[0]
#         totalPageNum = int(totalPageNum) + 1
#
#         return totalPageNum, title, docId
#
#     def download_img(self, totalPageNum, title, docId):
#         for pn in range(1, totalPageNum):
#             params = {'doc_id': docId, 'pn': pn, 'rn': 1, 'type': 'ppt', }
#             api_url = 'https://wenku.baidu.com/browse/getrequest'
#             r = self.session.get(api_url, params=params, headers=self.headers)
#             src = r.json()[0].get('zoom')
#             os.makedirs(title, exist_ok=True)
#             path = title + '/' + str(pn) + '.jpg'
#             urlretrieve(src, path)
#             print(f'正在提取第{pn}页，请稍等...')
#
#     # 文章去重
#     def set_word(self, path):
#         word_set = list()
#         with open(path, 'r', encoding='utf-8') as f:
#             for each_line in f:
#                 word_set.append(each_line)
#         result = list(set(word_set))
#         result.sort(key=word_set.index)
#         with open(path, 'w', encoding='utf-8') as f:
#             f.writelines(result)
#             print('done')
#
#     # 获取文字内容
#     def run_word(self):
#         print('开始尝试解析百度文库页面...\n')
#         start_url = input('输入百度文库中的连接：')
#         print('running...\n')
#         start_url = re.sub('wenku', 'wk', start_url)
#         html = self.get_html(start_url)
#         param, ranges, title = self.parse_html(html)
#         print(f'当前文章：{title}\n')
#         path = '百度文库/' + title + '.doc'
#         response = self.words_data(param, ranges)
#         self.get_words(response)
#         self.save_info(title, path)
#         self.set_word(path)
#         print('done!!!')
#         print('程序执行完毕！')
#
#     # 获取图片数据
#     def run_img(self):
#         print('开始尝试解析百度文库图片信息...\n')
#         start_url = input('输入百度文库中的连接：')
#         print('running...\n')
#         totalPageNum, title, docId = self.get_img(start_url)
#         self.download_img(totalPageNum, title, docId)
#         print('done!!!')
#         print('程序执行完毕！')
#
#
# if __name__ == '__main__':
#     wk = BaiduWk()
#     wk.run_word()
# 导入数据请求模块
import requests
# 导入正则表达式
import re
# 导入json
import json
# 导入时间模块
import time
import base64
import docx
"""
文字识别:
    百度云API接口 --> 免费领取资源的
    1. 注册登陆
    2. 选择文字识别
    3. 创建应用 领取资源
    4. 进入API文档
        - 获取token
        - 复制API代码
"""
doc = docx.Document()


def Content(content):
    """
    :param content: 图片二进制数据
    :return:
    """
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=xxxx&client_secret=xxxx"
    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    access_token = response.json()['access_token']
    print(access_token)
    '''
    通用文字识别（高精度版）
    '''
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    img = base64.b64encode(content)
    params = {"image":img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    json_data = requests.post(request_url, data=params, headers=headers).json()
    words_result = '\n'.join([i['words'] for i in json_data['words_result']])
    print(words_result)
    return words_result




"""
1. 发送请求, 模拟浏览器对于url地址发送请求
"""
# 模拟浏览器 --> 请求头, 直接复制
headers = {
    # 完整源码、解答、教程皆+VX：Python5180 记得验证备注AAA
    'Cookie': 'CLIENT_SYS_UN_ID=3rvhLGQlZ5CsGW2eHpmuAg==; __yjs_duid=1_0ce66bf3ca7c2306ce5da72ade1b4ba11685945826433; s_v=cdh%3D%3E27a30245%7C%7C%7Cvid%3D%3E1685945827928042385%7C%7C%7Cfsts%3D%3E1685945827%7C%7C%7Cdsfs%3D%3E25%7C%7C%7Cnps%3D%3E2; s_rfd=cdh%3D%3E27a30245%7C%7C%7Ctrd%3D%3Emax.book118.com%7C%7C%7Cftrd%3D%3Ebook118.com; s_s=cdh%3D%3E27a30245%7C%7C%7Clast_req%3D%3E1688127125%7C%7C%7Csid%3D%3E1688124093504555434%7C%7C%7Cdsps%3D%3E25',
    'Host': 'openapi.book118.com',
    'Pragma': 'no-cache',
    'Referer': 'https://*****/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}
for page in range(1, 14, 6):
    time.sleep(2)
    # 请求链接
    url = 'https://openapi.book118.com/getPreview.html'
    # 请求参数 --> 缩进 tab 取消缩进 shift+tab 复制当前行crtl + D
    data = {
        'project_id': '1',
        'aid': '569535184',
        't': '8684559560dd49bd42aeb2e85b6d6f06',
        'view_token': 'qKyQHm9Lw@hAGeaC16lOgvTEUQeFscw1',
        'page': page,
        'filetype': 'docx',
        # 'callback': 'jQuery183015452790725275278_1688127062003',
        '_': '1688127520232',
    }
    # 发送请求
    response = requests.get(url, params=data, headers=headers)
    """
    2. 获取数据, 获取服务器返回响应数据
        response.text 获取响应的文本数据
    3. 解析数据, 提取我们需要的内容 --> 图片链接
        re.findall('数据', '地方') 找到所有数据
            从什么地方, 去匹配找寻什么数据
        re.findall('jsonpReturn\((.*?)\)', response.text)
        \ 转义字符, 把含有特殊意义字符,转义成本身以外, 不含有其他特殊意义
        () 精确匹配
        .*? --> 可以匹配任意字符串 除了\n换行符
        正则匹配的数据, 返回列表

    """
    html_data = re.findall('jsonpReturn\((.*?)\)', response.text)[0]
    # 转成字典数据
    json_data = json.loads(html_data)
    for link in json_data['data'].values():
        link = 'https:' + link
        # 有时候加伪装可能还不到数据 <请求头参数加多了>
        img = requests.get(link).content
        words = Content(img).replace('原创力文档', '').replace('max.book118.com', '').replace('下载高清无水印', '')
        print(words)
        # 写入内容
        doc.add_paragraph(words)

doc.save('大学生电子商务实习报告.docx')
