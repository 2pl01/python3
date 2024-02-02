# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： dome.py
    @date：2024/01/31 17:38
    
"""
import cv2
from 文字识别 import img_str
from docx import Document

if __name__ == '__main__':
    # 创建窗口
    cv2.namedWindow("camera",1)

    #video ="http://admin:admin@192.168.0.48:80"
    capture = cv2.VideoCapture(0)
    capture.set(3,800)
    capture.set(4,600)
    content_list = []
    while True:
        success,img =capture.read()
        cv2.imshow('camera',img)

        #按键处理
        key =cv2.waitKey(10)
        if key == 27:
        #esc
            print('esc break')
            break
        if key == 32:
            #空格
            filename = 'frames.jpg'
            cv2.imwrite(filename,img)
            s=img_str.img_to_str(filename)
            print(s)
            content_list.append(s)
    doc = Document()
    content = '\n'.join(content_list)
    doc.add_paragraph(content)
    doc.save('data.docx')
    #释放掉摄像头
    capture.release()
    #关闭窗口
    cv2.destroyWindow("camera")




    # myVc=cv2.VideoCapture(1)
    # myVc.set(3,800)
    # myVc.set(4,600)
    # while True:
    #     check,frame = myVc.read()
    #     cv2.imshow('My Camera',frame)
    #     if (cv2.waitKey(1)==ord('q')):
    #         break
    # myVc.release()
    # cv2.destroyWindow()

