from tkinter import *
from tkinter.colorchooser import *

window = Tk()

window.title("Colorchooser Demo")


def choose_color():
    color = askcolor()
    print(color)


Button(window, text="Choose Color", command=choose_color).pack()

window.mainloop()


'''
选项：
color   用以为颜色选择对话框设置一个默认选择的颜色. 如果未指定 color 选项, 则默认选择颜色为灰色.

title	指定颜色对话框的标题栏文本.默认的标题为 “Colors”

parent	1. 如果不指定该选项，那么对话框默认显示在根窗口上
        2. 如果想要将对话框显示在子窗口 w 上，那么可以设置 parent=w
'''