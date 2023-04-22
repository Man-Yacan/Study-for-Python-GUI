# -*- coding: utf-8 -*-

"""
@Author: ManYacan
@Email: myxc@live.cn
@Website: www.manyacan.com
@time: 2023/04/16 19:26
@description: 
"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建一个PyQt对象，传进去的参数其实就是执行Python程序时，命令行里面的参数
    app = QApplication(sys.argv)

    # 创建界面对象
    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle("Yacan's First PyQt App")

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()
