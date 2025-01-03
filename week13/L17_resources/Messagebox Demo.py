from tkinter import *
from tkinter.messagebox import *

window = Tk()

window.title("Messagebox Demo")


def click_me():
    showinfo(title="Massagebox", message="显示一条信息")
    showerror(title="Massagebox", message="显示一条错误信息")
    showwarning(title="Massagebox", message="显示一条警告信息")

    askokcancel(title="Massagebox", message="询问用户操作是否继续. 选择 OK 则返回 True")
    askretrycancel(title="Massagebox", message="询问用户是否要重复操作. 选择 Retry 则返回 True")

    askquestion(title="Massagebox", message="显示一个问题")
    askyesno(title="Massagebox", message="显示一个问题. 选择 Yes 则返回 True")
    askyesnocancel(title="Massagebox", message="显示一个问题. 选择 Yes 则返回 True; 选择 Cancel 则返回 None")
    # 试一试：可在每一行前面添加 print()，将每次结果显示出来

Button(text="测试按钮", command=click_me).pack()


mainloop()

'''
消息框功能由 tkMessageBox 包提供, 其中包含了如下消息框类型:

askokcancel(title=None, message=None, **options)
询问用户操作是否继续. 选择 ok 则返回 True

askquestion(title=None, message=None, **options)
显示一个问题

askretrycancel(title=None, message=None, **options)
询问用户是否要重试操作. 选择 ok 则返回 True

askyesno(title=None, message=None, **options)
显示一个问题. 选择 ok 则返回 True

askyesnocancel(title=None, message=None, **options)
显示一个问题. 选择 ok 则返回 True; 选择 cancel 则返回 None

showerror(title=None, message=None, **options)
给出一条错误信息

showinfo(title=None, message=None, **options)
给出一条提示信息

showwarning(title=None, message=None, **options)
给出一条警告信息
'''
