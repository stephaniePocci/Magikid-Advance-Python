from tkinter import *

window = Tk()

window.title("Place_Layout")

# window.geometry('600x600')

Label(window, text="第0行，第0列", font=('Arial bold', 20),
      bg="red", fg="white").grid(row=0, column=0)
Label(window, text="第0行，第1列", font=('Arial bold', 20),
      bg="blue", fg="white").grid(row=0, column=1)
Label(window, text="第0行，第2列", font=('Arial bold', 20),
      bg="red", fg="white").grid(row=0, column=2)

Label(window, text="第1行，第0列", font=('Arial bold', 20),
      bg="blue", fg="white").grid(row=1, column=0)
Label(window, text="第1行，第1列", font=('Arial bold', 20),
      bg="orange", fg="white").grid(row=1, column=1)
Label(window, text="第1行，第2列", font=('Arial bold', 20),
      bg="blue", fg="white").grid(row=1, column=2)

Label(window, text="第2行，第0列", font=('Arial bold', 20),
      bg="red", fg="white").grid(row=2, column=0)
Label(window, text="第2行，第1列", font=('Arial bold', 20),
      bg="blue", fg="white").grid(row=2, column=1)
Label(window, text="第2行，第2列", font=('Arial bold', 20),
      bg="red", fg="white").grid(row=2, column=2)

window.mainloop()

'''
grid() 布局管理：表格式布局管理
'''