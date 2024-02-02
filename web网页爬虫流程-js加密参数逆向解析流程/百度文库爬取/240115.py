# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： 240115.py
    @date：2024/01/15 11:25
    
"""
import requests
import pprint
import re
headers = {
    "Referer": "https://wenku.baidu.com/search?lm=0&od=0&ie=utf-8&dyTabStr=MCwyLDEsMyw1LDYsNCw3LDgsOQ%3D%3D&word=python%E9%A2%98%E5%BA%93&_wkts_=1705288127396",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://wenku.baidu.com/view/129b8fb0bbf67c1cfad6195f312b3169a451ea98.html"
params = {
    "fr": "income1-doc-search",
    "_wkts_": "1705288132075",
    "wkQuery": "python题库"
}
response = requests.get(url, headers=headers, params=params).content.decode("UTF-8")

"""
https://wkbjcloudbos.bdimg.com/v1/docconvert4992/wk/45d2de80d62bdd722da714b8db9263a6/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Thu%2C%2029%20Feb%202024%2011%3A30%3A34%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2024-01-15T03%3A30%3A34Z%2F3600%2Fhost%2F17446c3e650bf100114fdce7be2055c142232004a48232e215a277fa8a23b3af&x-bce-range=0-37048&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTcwNTI5MzAzNCwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.j4JTngFJUNoi5ONXn%2BfOj3E0kEZNR19xqw7AG6IrT%2Bo%3D.1705293034
"pageLoadUrl":"https://wkbjcloudbos.bdimg.com/v1/docconvert4992/wk/45d2de80d62bdd722da714b8db9263a6/0.png?responseContentType=image%2Fpng&responseCacheControl=max-age%3D3888000&responseExpires=Thu%2C%2029%20Feb%202024%2011%3A39%3A22%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2024-01-15T03%3A39%3A22Z%2F3600%2Fhost%2Fa4d007bd915bea21eaa0705e356e96387ba3b2951ea76134d72a3e5a992a71b0&x-bce-range=0-14465&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTcwNTI5MzU2MiwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.XAnXK6C%2FbTZTwvAwY9w72xNhuty2yydqn78b6f1Nx5Y%3D.1705293562"
r'pageLoadUrl.*?:(https.*?0.json?.*?)\\'
json_data_1 = json.loads(re.findall('var pageData = (.*?);', html_data)[0])

"""
#print(response)



url_tony=re.findall('pageLoadUrl.*?(https.*?0.json?.*?)"',response)
#
print(url_tony)

for a in url_tony:
    url_new=a
    requests_2=requests.get(url_new).content
    content_2=re.findall('"c":"(.*?)".*?"y":(.*?),',requests_2.decode("UTF-8"))
    print(content_2)
    for b in content_2:
        print(b[0].encode('utf-8').decode('unicode-escape'))