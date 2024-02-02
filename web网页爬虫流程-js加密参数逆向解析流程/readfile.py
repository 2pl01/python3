# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： readfile.py
    @date：2023/11/23 8:22
    
"""
from typing import List

import requests
import json
import os
import tkinter
from tkinter import messagebox,font
# s="hellopython"
#
# for index in range(len(s)):
#     print (s[index],end='')
# exit()
# with open("音乐.txt", "r",encoding='utf-8') as f:
#     str_list =  [line.strip() for line in f]
# print(data)
# 定义字符串列表
# str_list = ["第一行数据", "第二行数据", "第三行数据", "第四行数据", "第五行数据"]


with open('PyQT5/DB/音乐.txt', 'r', encoding='gb2312') as f:
    str_list = f.readlines()
    # print( len(str_list)-1)
    # # len(str_list)
    # #print(str_list)
    # for line in str_list:
    # print(type(str_list))

# with open('音乐.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         # 在这里处理读取到的行
#         #print(line)
#         line.join(line)
        # print(line)
# 输出数据
# print(str_list,end='')
# print(str_list)
#exit()
# separator = '-----'
#
#
# def split_string_by_different_length(data, separator):
#     result = []
#     start = 0
#     while True:
#         next_index = data.find(separator, start)
#         if next_index == -1:
#             result.append(data[start:])
#             break
#         else:
#             result.append(data[start:next_index])
#             start = next_index + len(separator)
#     return result

# def get_data(str_r):
#     data = str_r
#     # new_lst = [s.split() for s in data]
#     # print(new_lst)
#     parts = data.split("----")
#     return parts
    # print(parts)


#
#     for part in str_rong.split("-----"):
# part.split(parts)
# print(part.split(parts))
# 处理列表中的每个元素


# song_name = parts[1]  # 提取歌曲名称
# artist = parts[2]  # 提取歌手名称
# duration = parts[3]  # 提取时长
# file_id = parts[4]  # 提取文件ID
# link = parts[5]  # 提取链接
# print(song_name)  # 输出：起风了
# print(artist)  # 输出：周深
# print(duration)  # 输出：05:11
# print(file_id)  # 输出：CD0AF377206DAAACAEE61B76D32360A3
# print(link)  # 输出：https://webfs.hw.kugou.com/202311230810/8388862aedffbe8f2a348b14ce516aac/v2/cd0af377206daaacaee61b76d32360a3/G324/M09/E7/8B/JJUEAGTDnb-AatcLAEwRZz-GrrQ519.mp3
# split_string_by_different_length(str_list, separator)
# data = str(split_string_by_different_length(str_list, separator))
# print(type(data))
# print(data)
data_list = []
new_string_list = []
#遍历字符串列表
for string in  str_list:
    # 将字符串按换行符分割成列表
    parts_str = string.replace('-----', ' ').replace('\n', '\n' + ' ')
    #print(parts_str)
    #data_list.append(parts)

#print(type(data_list))
    # print(part)
    parts =parts_str.split()
    # part = string.replace('-----', ' ').replace('\n', '\n' + ' ')
    # # 按顺序排序列表
    #
    print(parts)
    # ordered_list: list[str] = sorted(parts, key=lambda x: len(x))
    # ordered_list= sorted(parts, key=lambda x: len(x))
    # print(ordered_list)

    new_string_list.append(parts)


with open('PyQT5/DB/new_string_list.json', 'w') as file:
    json.dump(new_string_list, file)
# 输出有序的列表集合
    #print(ordered_list)
    # 创建一个新的列表，并将每个部分添加到列表中
    # new_list = []
    # for part in parts:



        #new_list.append(part.replace('"', '\\"').replace('\n', ' '))
# sorted_characters = sorted(parts)
# print(sorted_characters)
    #print(new_list)
# result = []
# current_line = ""
#
# for char in str_list:
#     if char == '\n':
#         result.append(current_line.replace('"', '\\"').replace('\n', ' '))
#         current_line = ""
#     else:
#         current_line += char
#
# result.append(current_line.replace('"', '\\"').replace('\n', ' '))
# print(result)
    #
# new_string_list = []
#
# for string in str_list:
#     new_string = string.replace('-----', ' ').replace('\n', '\n' + ' ')
#     new_string_list.append(new_string)
# print(type(new_string_list))
# with open('PyQT5/DB/new_string_list.json', 'w') as file:
#     json.dump(new_string_list, file)
# print(new_string_list)

exit()
def Sl_song():
    output = ''

    while True:
        num = input("请输入一个数字（输入 q 退出）：")
        if num == 'q':
            print("程序已退出。")
            break
        else:

            # num = int(input("请输入序号："))
            # 判断输入的序号是否在列表范围内
            num = int(num)
            if num >= 1 and num <= len(str_list):
                # 输出对应序号的字符串
                # print(type(line))
                # exit()
                str_rong = str_list[num - 1]
                str_r = split_string_by_different_length(str_rong, separator)
                # download(str_r[2],str_r[3],str_r[5])
                #print(str_r)
                download(str_r[1],str_r[5])
                #return str_r[5]

            else:
                print("输入的序号超出范围！")

    # while True:
    #     num = int(input("请输入序号："))
    #     if num==
    #     # 判断输入的序号是否在列表范围内
    #     if num >= 1 and num <= len(str_list):
    #         # 输出对应序号的字符串
    #         str_rong = str_list[num - 1]
    #         str_r =split_string_by_different_length(str_rong, separator)
    #         print(str_r[1])
    #     else:
    #         print("输入的序号超出范围！")
        # print(output)
        # print(row_index)


# print(type(str_list))
# for values in data.values():
#     print(values,end='')
# for index in range(len(data)):
#     print (data[index],end='')
# print(index)
#
#
# inp_num=str(input("请输入你要下载的歌曲的序号:"))
# if inp_num==data[0]:
#     print(inp_num)
#     print(data)
#
#
# if inp_num==data[0]:
#     print(data)
# row_index=temp[inp_num]
#
# if i==inp_num:
#     print(item
#     output += str(item)+"\n"

def download(sname,list):
    url = list
    sname=sname
    file_url = url
    # = 'downloaded_file.mp3'
    current_path = os.getcwd()
    folder_path = "music"
    #
    # # 如果文件夹不存在，则创建文件夹
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    response = requests.get(file_url, stream=True)

    #os.path.join(folder_name, file_name)

    with open(os.path.join(folder_path, sname+'.mp3'), 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
# def download(songname,play_url):
#     path = 'donmo下载歌曲/' + songname
#     #     创建一个文件夹
#     if not os.path.exists(path):
#         os.makedirs(path)
#
#     filename = os.path.join(path, songname + '.txt')
#     song = os.path.join(path, songname + '.mp3')1

#     with open(filename, 'w', encoding='utf-8') as fp:
#         # fp.write(lyrics)
#         fp.close()
#
#     with open(song, 'wb') as fp:
#         data = get_info(play_url).content
#         fp.write(data)
#         fp.close()
#
#     print('下载成功!!!!!!!!')
# def down(self):
#     try:
#         hash, filename = self.get_hash()
#         lyrics, play_url = self.get_song(hash)
#         self.download(self.input_name.get(), lyrics, play_url)
#         messagebox.showinfo('下载成功！！！路径为当前目录')
#     except:
#         messagebox.showinfo('下载失败，请重新加载！！！')



if __name__ == '__main__':
    Sl_song()
