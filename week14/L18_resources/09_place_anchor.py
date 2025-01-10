from tkinter import *

window = Tk()

window.title("Place_Layout")

window.geometry('400x400')

Label(window, text="North-West", font=('Arial bold', 20),
      bg="red", fg="white").place(x=0, y=0, anchor=NW)  # 这里的数字单位是像素
Label(window, text="North", font=('Arial bold', 20),
      bg="blue", fg="white").place(x=200, y=0, anchor=N)
Label(window, text="North-East", font=('Arial bold', 20),
      bg="red", fg="white").place(x=400, y=0, anchor=NE)

Label(window, text="West", font=('Arial bold', 20),
      bg="blue", fg="white").place(x=0, y=200, anchor=W)
Label(window, text="Center", font=('Arial bold', 20),
      bg="orange", fg="white").place(x=200, y=200, anchor=CENTER)
Label(window, text="East", font=('Arial bold', 20),
      bg="blue", fg="white").place(x=400, y=200, anchor=E)

Label(window, text="South-West", font=('Arial bold', 20),
      bg="red", fg="white").place(x=0, y=400, anchor=SW)
Label(window, text="South", font=('Arial bold', 20),
      bg="blue", fg="white").place(x=200, y=400, anchor=S)
Label(window, text="South-East", font=('Arial bold', 20),
      bg="red", fg="white").place(x=400, y=400, anchor=SE)

window.mainloop()

'''
anchor 代表容器的那个方位和需要放置的坐标进行对齐，默认是容器的左上角(nw方向)和设置的坐标对齐；
参数和pack，grid相同，都有9个；
'''