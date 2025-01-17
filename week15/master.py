from tkinter import *

window = Tk()

window.title("Frame Demo")

Label(window, text="Main window",
      bg='blue', fg='white',
      font=('Arial', 16)).pack()

# Create a main frame
frame_master = Frame(window, bg='yellow')
frame_master.pack()
Label(frame_master, text="main frame", bg='green').pack()

# Create a left subframe in the main frame
frame_left = Frame(frame_master)
frame_left.pack(side=LEFT)
Label(frame_left,
      text="Left subframe label 1", bg='red').pack()
Label(frame_left,
      text="Left subframe label 2", bg='blue').pack()

# Create a right subframe in the main frame
frame_right = Frame(frame_master)
frame_right.pack(side=RIGHT)
Label(frame_right,
      text="Right subframe label 1", bg='pink').pack()
Label(frame_right,
      text="Right subframe label 2", bg='pink').pack()

window.mainloop()
