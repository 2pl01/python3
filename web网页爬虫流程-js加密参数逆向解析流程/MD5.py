# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： MD5.py
    @date：2023/11/09 15:28
    
"""


import hashlib
import random
import time
import datetime

def gen_md5(word):
    word =''.join([x for x in word])
    encode_word = word.encode('utf-8')
    return hashlib.md5(encode_word).hexdigest()


def guid():
    num = 1 + random.random()
    res = hex(int(65536 * num))[3:]
    return res


GUID = guid() + guid() + "-" + guid() + "-" + guid() + "-" + guid() + "-" + guid() + guid() + guid()

def gen_params(word):
    timestamp = int(time.time() * 1000)
    dfid = '-'  # dfid经过本人多次测试发现为-即可
    # keyword = word
    mid = gen_md5(GUID)
   # t = f'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014bitrate=0callback=callback123clienttime={timestamp}clientver=1000dfid={dfid}filter=10inputtype=0iscorrection=1isfuzzy=0keyword={keyword}mid={mid}page=1pagesize=30platform=WebFilterprivilege_filter=0srcappid=2919token=userid=0uuid={mid}NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'

    #t=f'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014clienttime=1700214554clientver=1000dfid=0jHhKj0iduqI37p1J13hYaVCmid=93496844ccb7830073d08eca7cf9503bsrcappid=2919uuid=1700214553550{"userid":0,"plat":103,"m_type":0,"vip_type":0,"own_ads":{}}NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt
    signature = gen_md5(word)
    # params['clienttime'] = timestamp
    # params['dfid'] = dfid
    # params['keyword'] = keyword
    # params['mid'] = mid
    # params['uuid'] = mid
    # params['signature'] = signature
    # return params




# 获取当前时间戳（以毫秒为单位）
timestamp = datetime.datetime.now().timestamp() * 1000

# 对时间戳进行四舍五入并取整
rounded_timestamp = int(round(timestamp))

print(rounded_timestamp)



mid = gen_md5(GUID)
print(gen_params('NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014clienttime=1700214554clientver=1000dfid=0jHhKj0iduqI37p1J13hYaVCmid=93496844ccb7830073d08eca7cf9503bsrcappid=2919uuid=1700214553550{"userid":0,"plat":103,"m_type":0,"vip_type":0,"own_ads":{}}NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'))
#print(gen_md5('NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014clienttime=1700214554clientver=1000dfid=0jHhKj0iduqI37p1J1''3hYaVCmid=93496844ccb7830073d08eca7cf9503bsrcappid=2919uuid=1700214553550{"userid":0,"plat":103,"m_type":0,"vip_type":0,"own_ads":{}}NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'))


