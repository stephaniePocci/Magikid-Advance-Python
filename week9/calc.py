from tkinter import *

window = Tk()

Label(window, text ="1", font=('Arial', 26)).grid(row=0, column=0)
Label(window, text ="2", font=('Arial', 26)).grid(row=0, column=1)
Label(window, text ="3", font=('Arial', 26)).grid(row=1, column=0)
Label(window, text ="4", font=('Arial', 26)).grid(row=1, column=1)

# frame_master = Frame(window, bg='red')
# frame_master.pack()

# Label(frame_master, text ="test", font=('Arial', 26)).pack()




# frame_left = Frame(frame_master)
# frame_left.pack(side=LEFT)

# Label(frame_left, text ="test1", font=('Arial', 26)).pack()
# Label(frame_left, text ="test2", font=('Arial', 26)).pack()

# frame_right = Frame(frame_master)
# frame_right.pack(side=RIGHT)

# Label(frame_right, text ="test3", font=('Arial', 26)).pack()
# Label(frame_right, text ="test4", font=('Arial', 26)).pack()


window.mainloop()