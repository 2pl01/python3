# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： readCode.py
    @date：2024/02/02 15:18
    
"""
from pyzbar.pyzbar import decode
from PIL import Image
readData = decode(Image.open('barB.png'))
print(readData[θ].data.decode('utf-8'))