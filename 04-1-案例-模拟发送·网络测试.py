# -*- coding: utf-8 -*-

"""
@Author: ManYacan
@Email: myxc@live.cn
@Website: www.manyacan.com
@Time: 2023/04/21 22:29
@Description:
"""

import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QWidget):
    """
    模拟发送网络测试
    """

    # 声明一个信号，只能放在类的方法外面来定义
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()  # 继承父类
        self.build_ui()  # UI初始化
        self.msg_list = []  # 存放历史消息

    def build_ui(self):
        """
        构建系统界面UI
        """
        self.resize(500, 200)  # 定义窗口尺寸

        # 1、创建一个整体垂直布局容器
        container = QVBoxLayout()

        # 用来显示漏洞信息的文本窗口
        self.msg_div = QLabel("~~~")
        self.msg_div.resize(440, 15)
        self.msg_div.setWordWrap(True)  # 自动换行
        self.msg_div.setAlignment(Qt.AlignTop)  # 靠上
        self.msg_div.setStyleSheet("background-color: yellow; color: black;")

        # 创建一个滚动对象
        scroll = QScrollArea()
        scroll.setWidget(self.msg_div)

        # 创建垂直布局器，用来添加自动滚动条
        v_layout = QVBoxLayout()
        v_layout.addWidget(scroll)

        # 按钮
        h_layout = QHBoxLayout()
        btn = QPushButton("开始检测", self)
        h_layout.addStretch(1)  # 伸缩器
        h_layout.addWidget(btn)
        h_layout.addStretch(1)

        # 为按钮绑定事件
        btn.clicked.connect(self.check)

        # 操作将要显示的控件以及子布局器添加到container
        container.addLayout(v_layout)
        container.addLayout(h_layout)

        # 2、设置布局器
        self.setLayout(container)

        # 绑定信号和槽
        self.my_signal.connect(self.my_slot)

    def my_slot(self, msg):
        # 更新内容
        print(msg)
        self.msg_list.append(msg)
        self.msg_div.setText("<br>".join(self.msg_list))
        self.msg_div.resize(440, self.msg_div.frameSize().height() + 15)
        self.msg_div.repaint()  # 更新内容，如果不更新可能没有显示新内容

    def check(self):
        for i, ip in enumerate(["192.168.1.%d" % x for x in range(1, 255)]):
            msg = "模拟，正在检查 %s 上的漏洞...." % ip
            # print(msg)
            if i % 5 == 0:
                # 表示发射信号 对象.信号.发射(参数)
                self.my_signal.emit(msg + "【发现漏洞】")
            time.sleep(0.01)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWindow()
    w.show()

    app.exec()
