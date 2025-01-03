from tkinter import *
from tkinter.messagebox import *

window = Tk()

window.title("Messagebox Practice")


def click_me():
    showinfo(title="Massagebox", message="showinfo()\n显示一条信息")
    showerror(title="Massagebox", message="showerror()\n显示一条错误信息")
    showwarning(title="Massagebox", message="showwarning()\n显示一条警告信息")

    askquestion(title="Massagebox", message="askquestion()\n显示一个问题")

    askyesno(title="Massagebox", message="askyesno()\n显示一个问题. 选择 Yes 则返回 True")
    askyesnocancel(title="Massagebox", message="askyesnocancel()\n显示一个问题. 选择 Yes 则返回 True; 选择 Cancel 则返回 None")

    askokcancel(title="Massagebox", message="askokcancel()\n询问用户操作是否继续. 选择 OK 则返回 True")
    askretrycancel(title="Massagebox", message="askretrycancel()\n询问用户是否要重复操作. 选择 Retry 则返回 True")
    # 试一试：可在每一行前面添加 print()，将每次结果显示出来


Button(text="测试按钮", command=click_me).pack()

mainloop()

'''
options（选项）

default	    1. 设置默认的按钮（也就是按下回车响应的那个按钮）
            2. 默认是第一个按钮（像“确定”，“是”或“重试”）
            3. 可以设置的值根据对话框函数的不同可以选择：CANCEL，IGNORE，OK，NO，RETRY 或 YES

icon	    1. 指定对话框显示的图标
            2. 可以指定的值有：ERROR，INFO，QUESTION 或 WARNING
            3. 注意：不能指定自己的图标
            
parent	    1. 如果不指定该选项，那么对话框默认显示在根窗口上
            2. 如果想要将对话框显示在子窗口 w 上，那么可以设置 parent=w
'''
