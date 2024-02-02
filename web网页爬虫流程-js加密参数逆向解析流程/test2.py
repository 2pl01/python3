# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： test2.py
    @date：2023/11/24 11:54
    
"""
import os

# 要检查的文件夹路径
folder_path = "/path/to/folder"

# 如果文件夹不存在，则创建文件夹
if not os.path.exists(folder_path):
    os.makedirs(folder_path)