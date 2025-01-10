from tkinter import *

window = Tk()

window.title("pack_expand")

window.geometry("150x150")

Label(window, text="Label-1", bg='yellow').pack()
Label(window, text="Label-2", font=('Arial', 16),
       bg='green').pack(expand="yes")
Label(window, text="Label-3", bg='yellow').pack(expand="no")

window.mainloop()

'''
expand参数表示的是容器在整个窗口上，将容器放置在剩余空闲位置上的中央(包括水平和垂直方向)
expand=1或者expand=“yes”，表示放置在中央
expand=0或者expand=“no”，表示默认不扩展
'''
