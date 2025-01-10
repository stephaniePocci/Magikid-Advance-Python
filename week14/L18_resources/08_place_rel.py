from tkinter import *

window = Tk()

window.title("Place_Layout")

window.geometry('600x600')

Label(window, text="North-West", font=('Arial bold', 20),
      bg="red", fg="white").place(relx=0, rely=0, relwidth=0.33, relheight=0.33)  # 这里的数字单位是像素
Label(window, text="North", font=('Arial bold', 20),
      bg="blue", fg="white").place(relx=(1/3), rely=0, relwidth=0.33, relheight=0.33)
Label(window, text="North-East", font=('Arial bold', 20),
      bg="red", fg="white").place(relx=(2/3), rely=0, relwidth=0.33, relheight=0.33)

Label(window, text="West", font=('Arial bold', 20),
      bg="blue", fg="white").place(relx=0, rely=(1/3), relwidth=0.33, relheight=0.33)
Label(window, text="Center", font=('Arial bold', 20),
      bg="orange", fg="white").place(relx=(1/3), rely=(1/3), relwidth=0.33, relheight=0.33)
Label(window, text="East", font=('Arial bold', 20),
      bg="blue", fg="white").place(relx=(2/3), rely=(1/3), relwidth=0.33, relheight=0.33)

Label(window, text="South-West", font=('Arial bold', 20),
      bg="red", fg="white").place(relx=0, rely=(2/3), relwidth=0.33, relheight=0.33)
Label(window, text="South", font=('Arial bold', 20),
      bg="blue", fg="white").place(relx=(1/3), rely=(2/3), relwidth=0.33, relheight=0.33)
Label(window, text="South-East", font=('Arial bold', 20),
      bg="red", fg="white").place(relx=(2/3), rely=(2/3), relwidth=0.33, relheight=0.33)

window.mainloop()
