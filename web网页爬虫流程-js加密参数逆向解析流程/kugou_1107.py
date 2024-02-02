# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： kugou_1107.py
    @date：2023/11/07 15:15
    
"""
import requests
import json
#伪装自己
headers={
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
}
#list_url1 ='https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime=1699341076779&mid=8462a9e79aaab05633c9bae2d5e9bf14&uuid=8462a9e79aaab05633c9bae2d5e9bf14&dfid=4FHxl53HFHow3tVd9r3EnzHw&keyword=%E5%A4%A7%E9%B1%BC+%E5%91%A8%E6%B7%B1&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature=69ddcf5375981b74208457a1ae34022a'

list_url ='https://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord={}'
#list_url='https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime=1699427742600&mid=8462a9e79aaab05633c9bae2d5e9bf14&uuid=8462a9e79aaab05633c9bae2d5e9bf14&dfid=4FHxl53HFHow3tVd9r3EnzHw&keyword=null&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature=a35a91fb7351056144aeb4faa3c93ea6'

list_resp = requests.get(list_url,headers=headers)


song_list_utf8 = json.loads(list_resp.text[12:-2].encode('utf-8').decode('utf-8').encode('gbk', 'ignore').decode('gbk'))
#print(song_list_utf8)
#song_list_utf8 =json.loads(list_resp.text[12:-2].encode('utf-8').decode('utf-8').encode('gbk', 'ignore').decode('gbk'))
song_list=song_list_utf8['data']['lists']

for i,s in enumerate(song_list):
    print(f'{i+1}-----{s.get("SongName")}-----{s.get("FileHash")}')
#print(song_list_utf8)
print(song_list)


if __name__ == '__main__':
    # try:
        keyword = input('请输入要搜索的歌曲名称：')
    #     hash_value, album_id = get_data(get_url(keyword))
    #
    #     get_mp3(hash_value, album_id)
    # except Exception as e:
    #     print('请输入正确歌曲名称。')

"""

#音乐url
m_url='https://webfs.hw.kugou.com/202311071523/b846d941054417b20973e5454c5f2089/part/0/960111/KGTX/CLTX001/clip_bfbdd3df47727b701d4480ea36a8f73b.mp3'
#发送请求到服务器，获取资源
m_resp = requests.get(m_url,headers=headers)
#服务器回应的数据--保存数据
with open('zzz.mp3','wb') as f:
    f.write(m_resp.content)
"""

