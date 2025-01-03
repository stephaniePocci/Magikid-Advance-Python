from tkinter.filedialog import *
from tkinter import *

window = Tk()

window.title("Filedialog Demo")


def open_file():
    files = askopenfilename()
    print(files)


btn = Button(text="Open File", command=open_file)
btn.pack()

mainloop()


'''
方法：
askdirectory():选择目录，返回目录名

askopenfile():选择打开什么文件，返回IO流对象
askopenfiles():选择打开多个文件，以列表形式返回多个IO流对象

askopenfilename():选择打开什么文件，返回文件名
askopenfilenames():选择打开多个文件，以元组形式返回多个文件名

asksaveasfilename():选择以什么文件名保存，返回文件名
asksaveasfile():选择以什么文件保存，创建文件并返回文件流对象
------------------------------------------------------
选项：
defaultextension	1. 指定文件的后缀
                    2. 例如：defaultextension=".jpg"，那么当用户输入一个文件名 "logo" 的时候，文件名会自动添加后缀为 "logo.jpg"
                    3. 注意：如果用户输入文件名包含后缀，那么该选项不生效

filetypes	        1. 指定筛选文件类型的下拉菜单选项
                    2. 该选项的值是由 2 元祖构成的列表
                    3. 每个 2 元祖由（类型名，后缀）构成，例如：filetypes=[("PNG", ".png"), ("JPG", ".jpg"), ("GIF", ".gif")]

initialdir	        1. 指定打开/保存文件的默认路径
                    2. 默认路径是当前文件夹

parent	            1. 如果不指定该选项，那么对话框默认显示在根窗口上
                    2. 如果想要将对话框显示在子窗口 w 上，那么可以设置 parent=w

title	            指定文件对话框的标题栏文本
'''