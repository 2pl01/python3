# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： test.py
    @date：2023/11/07 11:24
    
"""
import requests
import re
import json
import time
import execjs


def get_signature(text):
    """
    获取signature值
    :param text: 格式化之后的字符串
    :return: 返回酷狗网站上加密后的signature
    """
    # 读取js文件内容
    with open("kugou.js", "r", encoding='utf-8') as f:
        js_str = f.read()

    # 通过js文件中逻辑数据，对文件进行加密
    if js_str:
        js_obj = execjs.compile(js_str)
        return js_obj.call('faultylabs.MD5', text)
def get_url(keyword):
    """
    获取搜索之后的url
    :param keyword: 搜索词，如晴天
    :return: 返回完整的url地址
    """
    search = "https://complexsearch.kugou.com/v2/search/song?callback=callback123&keyword={keyword}&page=1&pagesize=30&bitrate=0&isfuzzy=0&tag=em&inputtype=0&platform=WebFilter&userid=-1&clientver=2000&iscorrection=1&privilege_filter=0&srcappid=2919&clienttime={time}&mid={time}&uuid={time}&dfid=-&signature={signature}"
    #search1="https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime=1699329172270&mid=8462a9e79aaab05633c9bae2d5e9bf14&uuid=8462a9e79aaab05633c9bae2d5e9bf14&dfid=4FHxl53HFHow3tVd9r3EnzHw&keyword=%E8%B5%B7%E9%A3%8E%E4%BA%86%C2%A0%E5%91%A8%E6%B7%B1&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature=2cc73d12d2a33174addae4567cf95b32"


    key_code = "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtbitrate=0callback=callback123clienttime={time}clientver=2000dfid=-inputtype=0iscorrection=1isfuzzy=0keyword={keyword}mid={time}page=1pagesize=30platform=WebFilterprivilege_filter=0srcappid=2919tag=emuserid=-1uuid={time}NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"

    # 获得13位时间戳
    millis = str(round(time.time() * 1000))
    p = key_code.format(time=millis, keyword=keyword)
    signature = get_signature(p)
    # print(signature)

    search_url = search.format(keyword=keyword, time=millis, signature=signature)
    return search_url
def get_data(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
        'referer': 'https://www.kugou.com/',
        'authority': 'complexsearch.kugou.com',
    }

    res = requests.get(url=url, headers=headers)

    # 将获取的数据转为json格式
    data = re.findall('callback123\((.*)\)', res.text, re.S)[0]
    json_data = json.loads(data)['data']

    hash_value = json_data['lists'][0]['FileHash'].lower()
    album_id = json_data['lists'][0]['AlbumID']
    return hash_value, album_id


def get_mp3(hash_value, album_id):
    """
    获取MP3音频文件
    :param hash_value: 传入哈希值
    :param album_id:  传入album id
    :return: none
    """
    url = 'https://wwwapi.kugou.com/yy/index.php'

    params = {
        'r': 'play/getdata',
        'callback': 'jQuery191019800824574510756_1612519333214',
        'hash': str(hash_value),
        'dfid': '4FHxl53HFHow3tVd9r3EnzHw',
        'mid': '8462a9e79aaab05633c9bae2d5e9bf14',
        'platid': '4',
        'album_id': str(album_id),
    }

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
        'referer': 'https://www.kugou.com/',
        'authority': 'wwwapi.kugou.com',
    }
    res = requests.post(url=url, params=params, headers=headers)

    data = re.findall('jQuery191019800824574510756_1612519333214\((.*?)\);', res.text, re.S)[0]
    json_data = json.loads(data)

    audio_name = json_data['data']['audio_name']
    play_url = json_data['data']['play_url']

    save_mp3(audio_name, play_url)


def save_mp3(audio_name, play_url):
    """
    保持MP3文件
    :param audio_name: 传入命名
    :param play_url: 传入音频url
    :return: none
    """
    content = requests.get(play_url).content
    with open(audio_name + '.mp3', mode='ab') as f:
        f.write(content)


if __name__ == '__main__':
    try:
        keyword = input('请输入要搜索的歌曲名称：')
        hash_value, album_id = get_data(get_url(keyword))

        get_mp3(hash_value, album_id)
    except Exception as e:
        print('请输入正确歌曲名称。')

# if __name__ == '__main__':
#     str='NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014bitrate=0callback=callback123clienttime=1699328039837clientver=1000dfid=4FHxl53HFHow3tVd9r3EnzHwfilter=10inputtype=0iscorrection=1isfuzzy=0keyword=起风了 周深mid=8462a9e79aaab05633c9bae2d5e9bf14page=1pagesize=30platform=WebFilterprivilege_filter=0srcappid=2919token=userid=0uuid=8462a9e79aaab05633c9bae2d5e9bf14NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'
#     print( get_signature(str))
