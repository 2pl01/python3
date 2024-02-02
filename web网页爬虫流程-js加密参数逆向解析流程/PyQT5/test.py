# coding=utf-8
"""
    @project: python3
    @Author："东家“
    @file： test.py
    @date：2023/12/05 16:34
    
"""
#-*- codeing = utf-8 -*-
#@Time : 2020/5/13 20:20
#@Author : dele
#@File : music.py
#@Software: PyCharm

# 功能实现
# 搜索 https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=lemon
# 歌曲ID https://y.qq.com/n/yqq/song/000akynZ2Rbro5.html
# 解析 http://www.douqq.com/qqmusic/qqapi.php
import os.path
import sys

from PyQt5.QtWidgets import QApplication,QWidget,QDesktopWidget,QVBoxLayout,QHBoxLayout
from PyQt5.QtWidgets import QPushButton,QLineEdit,QTableWidget,QTableWidgetItem,QLabel

BASE_DIR=os.path.dirname(os.path.realpath(sys.argv[0]))

STATUS_MAPPING={
    0:"初始化中",
    1:"待执行",
    2:"正在执行",
    3:"完成并提醒",
    10:"异常并停止",
    11:"初始化失败",
}

# 界面设计
class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        #窗体标题和尺寸
        self.setWindowTitle('NB的XX系统')
        #窗体的尺寸
        self.resize(1228,450)
        #窗体位置
        qr=self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.show()
        #创建布局
        layout =QVBoxLayout()
        #调用顶部菜单
        layout.addLayout(self.init_header())
        # 2.创建上面标题布局
        #调用输入框
        layout.addLayout(self.init_form())
        #调用表格
        layout.addLayout(self.init_table())
        #调用底部菜单
        layout.addLayout(self.init_footer())
        #添加弹簧
        #layout.addStretch()

        #给窗体设置元素的排列方式
        self.setLayout(layout)
    def init_header(self):
        # 创建顶部菜单布局
        header_layout = QHBoxLayout()
        # 1.1创建按钮，加入header_layout
        btn_start = QPushButton("开始")
        header_layout.addWidget(btn_start)
        # 1.2创建按钮，加入header_layout
        btn_stop = QPushButton("停止")
        header_layout.addWidget(btn_stop)
        # 弹簧
        header_layout.addStretch()
        return header_layout
    def init_form(self):
        # 2.1输入框
        form_layout = QHBoxLayout()
        txt_asin = QLineEdit()
        txt_asin.setPlaceholderText("请输入商品ID和价格，例如：B8818JJQQ8=88")
        form_layout.addWidget(txt_asin)

        # 2.2添加按钮
        btn_add = QPushButton("添加")
        form_layout.addWidget(btn_add)
        return  form_layout
    def init_table(self):
        # 3.创建中间表格
        table_layout = QHBoxLayout()
        # 3.1创建表格
        table_widget = QTableWidget(0, 8)
        tab_header = [
            {"field": "asin", "text": "ASIN", 'width': 120},
            {"field": "title", "text": "标题", 'width': 150},
            {"field": "url", "text": "URL", 'width': 400},
            {"field": "price", "text": "底价", 'width': 100},
            {"field": "success", "text": "成功次数", 'width': 100},
            {"field": "error", "text": "503次数", 'width': 100},
            {"field": "status", "text": "状态", 'width': 100},
            {"field": "frequency", "text": "频率(N秒/次)", 'width': 100},
        ]
        for idx, info in enumerate(tab_header):
            item = QTableWidgetItem()
            item.setText(info['text'])
            table_widget.setHorizontalHeaderItem(idx, item)
            table_widget.setColumnWidth(idx, info['width'])
        table_layout.addWidget(table_widget)
        return table_layout
    def init_footer(self):
        # 底部菜单
        footer_layout = QHBoxLayout()
        label_status = QLabel("未检测", self)
        footer_layout.addWidget(label_status)
        footer_layout.addStretch()

        btn_reinit = QPushButton("重新初始化")
        footer_layout.addWidget(btn_reinit)
        # btn_reinit.clicked.connect(self.event_reinit_click)
        btn_recheck = QPushButton("重新检测")
        footer_layout.addWidget(btn_recheck)
        # btn_recheck.clicked.connect(self.event_recheck_click)
        btn_reset_count = QPushButton("次数清零")
        footer_layout.addWidget(btn_reset_count)
        # btn_reset_count.clicked.connect(self.event_reset_count_click)
        btn_delete = QPushButton("删除检测项")
        footer_layout.addWidget(btn_delete)
        # btn_delete.clicked.connect(self.event_delete_click)
        btn_alert = QPushButton("SMTP报警配置")
        footer_layout.addWidget(btn_alert)
        return footer_layout




if __name__ == '__main__':
    app=QApplication(sys.argv)
    window =Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())


    sys.exit(app.exec())




