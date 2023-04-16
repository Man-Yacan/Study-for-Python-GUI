# -*- coding: utf-8 -*-

"""
@Author: ManYacan
@Email: myxc@live.cn
@Website: www.manyacan.com
@time: 2023/04/16 16:29
@description: 
"""

import tkinter as tk


class App:
    def __init__(self, master):
        self.master = master
        master.title("My App")

        self.label = tk.Label(master, text="Hello World!")
        self.label.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
