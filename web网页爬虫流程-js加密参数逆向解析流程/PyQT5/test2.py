# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： test2.py
    @date：2023/12/11 9:47
    
"""
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QListView
from PyQt5.QtCore import Qt
import sys
class MusicSearcher:
    def __init__(self):
        self.search_results = []  # 假设这是存储搜索结果的变量

    def search(self, query):
        # 在这里执行音乐搜索，并把结果存储在 self.search_results
        pass

    def download(self, item):
        # 在这里执行下载功能
        pass

class MusicSearch(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('音乐搜索')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.search_input = QLineEdit()
        self.search_button = QPushButton('搜索')
        self.search_button.clicked.connect(self.search)

        self.layout.addWidget(self.search_input)
        self.layout.addWidget(self.search_button)

        self.result_list = QListView()
        self.layout.addWidget(self.result_list)

        self.music_searcher = MusicSearcher()

    def search(self):
        query = self.search_input.text()
        self.music_searcher.search(query)
        self.show_results()

    def show_results(self):
        self.result_list.clear()
        for item in self.music_searcher.search_results:
            self.result_list.addItem(item)

    def download(self):
        pass  # 需要你根据 `MusicSearcher` 的 `download` 方法来实现这个函数，以响应下载按钮的点击事件。




if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = MusicSearch()
    window.show()
    sys.exit(app.exec())