from tkinter import *

window = Tk()

window.title("显示图片")

width = 600
height = 600

screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
window.geometry(alignstr)

# img = r'/Users/liaokaige/Documents/PycharmProjects/TkinterProject_S02L11/logo.png'
# photo = PhotoImage(file=img)  # 加载图片的绝对路径
# photo = PhotoImage(file="logo.png")  # 加载图片的相对路径(在同一文件夹下)
labelImg = Label(window, text="test")
labelImg.pack(side=TOP)

window.mainloop()
