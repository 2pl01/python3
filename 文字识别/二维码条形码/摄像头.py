# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： 摄像头.py
    @date：2024/02/02 15:14
    
"""
import cv2
from pyzbar.pyzbar import decode
myVC= cv2.VideoCapture(0)
myVC.set(3,160)
myVC.set(4,120)
while True:
    check,frame = myVC.read()
    cv2. imshow( 'My Camera', frame)
    for barcode in decode(frame):
        print(barcode.data.decode('utf-8'))
    if(cv2.waitKey(1)==ord('q')):
        break
myVC.release()
cv2.destroyAllWindows()
