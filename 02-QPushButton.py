# -*- coding: utf-8 -*-

"""
@Author: ManYacan
@Email: myxc@live.cn
@Website: www.manyacan.com
@time: 2023/04/16 20:06
@description: 
"""

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QDesktopWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    # 1、设置窗口
    w.setWindowTitle("第一个PyQt程序")  # 设置窗口标题
    w.resize(800, 500)  # 窗口的大小
    w.setWindowIcon(QIcon('favicon.ico'))  # 设置图标
    # w.move(0, 0)  # 将窗口设置在屏幕的左上角

    # 调整窗口在屏幕中央显示
    center_pointer = QDesktopWidget().availableGeometry().center()
    x = center_pointer.x()
    y = center_pointer.y()
    old_x, old_y, width, height = w.frameGeometry().getRect()
    w.move(int(x - width / 2), int(y - height / 2))  # 输入必须为整数，否则报错，move(self, ax: int, ay: int)

    # 2.1、控件-按钮：在窗口里面添加控件
    btn = QPushButton("登录")
    btn.setParent(w)  # 设置按钮的父亲是当前窗口，等于是添加到窗口中显示
    btn.setGeometry(50, 80, 70, 30)  # 设置按钮位置

    # 2.2、控件-文本：下面创建一个Label（纯文本），在创建的时候指定了父对象
    label = QLabel("账号: ", w)
    label.setGeometry(20, 30, 40, 30)  # 显示位置与大小 ： x, y , w, h

    # 2.3、控件-文本框：
    edit = QLineEdit(w)
    edit.setPlaceholderText("请输入账号")
    edit.setGeometry(80, 30, 200, 30)

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()
