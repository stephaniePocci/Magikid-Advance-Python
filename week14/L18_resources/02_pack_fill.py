from tkinter import *

window = Tk()

window.title("pack_fill")

window.geometry('400x300')

Label(window, text=".pack(side=TOP)",
      bg="orange", fg="white").pack(side=TOP, fill=X)
Label(window, text=".pack(side=BOTTOM)",
      bg="red", fg="white").pack(side=BOTTOM, fill=X)
Label(window, text=".pack(side=LEFT)",
      bg="blue", fg="white").pack(side=LEFT, fill=Y)
Label(window, text=".pack(side=RIGHT)",
      bg="green", fg="white").pack(side=RIGHT, fill=Y)

Label(window, text="中间", font=('Arial', 16),
      bg='yellow').pack(expand=1)

window.mainloop()
