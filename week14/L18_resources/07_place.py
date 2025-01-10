from tkinter import *

window = Tk()

window.title("Place_Layout")

window.geometry('600x600')

Label(window, text="North-West", font=('Arial bold', 20),
      bg="red", fg="white").place(x=0, y=0, width=200, height=200)  # 这里的数字单位是像素
Label(window, text="North", font=('Arial bold', 20),
      bg="blue", fg="white").place(x=200, y=0, width=200, height=200)
Label(window, text="North-East", font=('Arial bold', 20),
      bg="red", fg="white").place(x=400, y=0, width=200, height=200)

Label(window, text="West", font=('Arial bold', 20),
      bg="blue", fg="white").place(x=0, y=200, width=200, height=200)
Label(window, text="Center", font=('Arial bold', 20),
      bg="orange", fg="white").place(x=200, y=200, width=200, height=200)
Label(window, text="East", font=('Arial bold', 20),
      bg="blue", fg="white").place(x=400, y=200, width=200, height=200)

Label(window, text="South-West", font=('Arial bold', 20),
      bg="red", fg="white").place(x=0, y=400, width=200, height=200)
Label(window, text="South", font=('Arial bold', 20),
      bg="blue", fg="white").place(x=200, y=400, width=200, height=200)
Label(window, text="South-East", font=('Arial bold', 20),
      bg="red", fg="white").place(x=400, y=400, width=200, height=200)

window.mainloop()

'''
place() 布局管理：指定组件的绝对位置
x=, y=           代表窗口大小所对应的x, y绝对坐标
relx=, rely=     代表窗口大小所对应的x, y坐标比例

width            代表容器的宽度，是窗口坐标值单位
heigh            代表容器的高度，是窗口坐标值单位，和容器定义中的heigh有区别
relwidth         代表容器宽度是窗口宽度的相对值
relheigh         代表容器高度是窗口高度的相对值
'''