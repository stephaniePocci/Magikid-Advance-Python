from tkinter import *

window = Tk()

window.title("Place_Layout")

# window.geometry('600x600')

"""Label(window, text="第0行，第0列", font=('Arial bold', 20),
      bg="red", fg="white").grid(row=0, column=0)
Label(window, text="第0行，第1列", font=('Arial bold', 20),
      bg="orange", fg="white").grid(row=0, column=1)"""
"""Label(window, text="第0行，第2列", font=('Arial bold', 20),
      bg="blue", fg="white").grid(row=0, column=2)
Label(window, text="第0行，第3列", font=('Arial bold', 20),
      bg="red", fg="white").grid(row=0, column=3)"""

Label(window, text="第一个合并", font=('Arial bold', 20), width=16, 
      bg="green", fg="white").grid(row=0, column=0, rowspan=2, columnspan=2)

Label(window, text="第二个合并", font=('Arial bold', 20), width=16,
      bg="green", fg="white").grid(row=0, column=2, rowspan=1, columnspan=4)

"""Label(window, text="第1行，第0列", font=('Arial bold', 20),
      bg="orange", fg="white").grid(row=1, column=0)
Label(window, text="第1行，第1列", font=('Arial bold', 20),
      bg="blue", fg="white").grid(row=1, column=1)"""
Label(window, text="第1行，第2列", font=('Arial bold', 20),
      bg="red", fg="white").grid(row=1, column=2)
Label(window, text="第1行，第3列", font=('Arial bold', 20),
      bg="orange", fg="white").grid(row=1, column=3)

Label(window, text="第2行，第0列", font=('Arial bold', 20),
      bg="blue", fg="white").grid(row=2, column=0)
Label(window, text="第2行，第1列", font=('Arial bold', 20),
      bg="red", fg="white").grid(row=2, column=1)
Label(window, text="第2行，第2列", font=('Arial bold', 20),
      bg="orange", fg="white").grid(row=2, column=2)
Label(window, text="第2行，第3列", font=('Arial bold', 20),
      bg="blue", fg="white").grid(row=2, column=3)

window.mainloop()

'''
rowspan, columnspan
这2个参数配合row和column使用，表示将对应行列单元格的row或者column合并为一个使用。
'''