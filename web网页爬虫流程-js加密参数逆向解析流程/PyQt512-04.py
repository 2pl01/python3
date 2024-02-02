# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： PyQt512-04.py
    @date：2023/12/04 15:28
    
"""
from PyQt5.QtWidgets import QApplication, QMainWindow
from untitled import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWinsow = MainWindow()
    MainWinsow.show()
    sys.exit(app.exec_())
