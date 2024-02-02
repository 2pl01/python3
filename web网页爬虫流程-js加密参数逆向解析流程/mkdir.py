# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： mkdir.py
    @date：2023/11/27 9:51
    
"""
import os
import shutil

current_path = os.getcwd()

print(current_path)
folder_path = "music"
if not os.path.exists(folder_path):
    os.mkdir(folder_path)