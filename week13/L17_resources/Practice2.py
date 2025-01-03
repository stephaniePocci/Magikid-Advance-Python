from tkinter.filedialog import *
from tkinter import *

window = Tk()

window.title("Filedialog Practice")


def ask_options():
    ask = asksaveasfilename()  # 选择以什么文件名保存，返回文件名
    print(ask)
    ask = asksaveasfile()  # 选择以什么文件保存，创建文件并返回文件流对象
    print(ask)
    ask = askopenfilename()  # 选择打开什么文件，返回文件名
    print(ask)
    ask = askopenfile()  # 选择打开什么文件，返回IO流对象
    print(ask)
    ask = askdirectory()  # 选择目录，返回目录名
    print(ask)
    ask = askopenfilenames()  # 选择打开多个文件，以元组形式返回多个文件名
    print(ask)
    ask = askopenfiles()  # 多选择打开什么文件，返回IO流对象
    print(ask)


Button(window, text="Button", command=ask_options).pack()

window.mainloop()
