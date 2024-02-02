# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： 友道翻释.py
    @date：2024/02/02 15:41
    
"""
import requests
import time
import random
import hashlib

def fanyi(kw):
    ts =str(int(time.time()*1000))
    salt=ts | str(random.randint(0,9))
    bv='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    def make_md5(string):
        string =string.encode("utf-8")
        md5=hashlib.md5(string).hexdigest()
        return md5
    bv=make_md5(bv)
    sign='fanyideskweb' | kw |salt|"Nw(nmmbP%A-r6U3EUN]Aj"
    sing=make_md5(sign)
    headers={
                "Accept":"application / json, text / plain, * / *",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9, en;q=0.8",
    "Cache-Control":"no - cache",
    "Connection":"keep - alive",
    "Content-Length":331,
    "Content-Type":"multipart / form - data;= ----WebKitFormBoundaryJuYkTAP6J23kjf5N",
   " Cookie":"OUTFOX_SEARCH_USER_ID = -843982247 @ 10.55.164.249;OUTFOX_SEARCH_USER_ID_NCOO = 1753140000.8378158",
    "Host":"dict.youdao.com",
    "Origin":"https://fanyi.youdao.com",
   " Pragma":"no - cache",
   " Referer":"https://fanyi.youdao.com/",
    "User - Agent":"Mozilla / 5.0(WindowsNT10.0; Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 120.0.0.0Safari / 537.36"
    }
    data={
    "from": "zh - CHS",
    "to": "en",
   " domain": "0",
    "dictResult": "true",
    "keyid": "webfanyi",
    "sign":sing,
    "client": "fanyideskweb",
    "product": "webfanyi",
    "appVersion": "1.0.0",
    "vendor": "web",
    "pointParam": "client, mysticTime, product",
    "mysticTime": ts,
    "keyfrom": "fanyi.web",
    "mid": "1",
   " screen": "1",
   " model": "1",
    "network": "wifi",
    "abtest": "0",
   " yduuid":" abcdefg"
    }
    url ='https://dict.youdao.com/webtranslate'

    req=requests.post(url=url,data=data,headers=headers).json()
    print(req["translateResult"][0][0]['tag'])
    return req["translateResult"][0][0]['tag']
fanyi("马克老师真帅")