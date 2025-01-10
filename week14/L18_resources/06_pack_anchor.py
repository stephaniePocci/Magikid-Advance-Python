from tkinter import *

window = Tk()

window.title("pack_anchor")

window.geometry('600x600')

Label(window, text=".pack(anchor=NW)", width=20, height=3,  # NW → north west
      bg="red", fg="white").pack(anchor=NW)
Label(window, text=".pack(anchor=N)", width=20, height=3,  # N → north
      bg="blue", fg="white").pack(anchor=N)
Label(window, text=".pack(anchor=NE)", width=20, height=3,  # NE → north east
      bg="red", fg="white").pack(anchor=NE)

Label(window, text=".pack(anchor=W)", width=20, height=3,  # W → west
      bg="blue", fg="white").pack(anchor=W)
Label(window, text=".pack(anchor=CENTER)", width=20, height=3,  # CENTER
      bg="orange", fg="white").pack(anchor=CENTER)
Label(window, text=".pack(anchor=E)", width=20, height=3,  # E → east
      bg="blue", fg="white").pack(anchor=E)

Label(window, text=".pack(anchor=SW)", width=20, height=3,  # SW → south west
      bg="red", fg="white").pack(anchor=SW)
Label(window, text=".pack(anchor=S)", width=20, height=3,  # S → south
      bg="blue", fg="white").pack(anchor=S)
Label(window, text=".pack(anchor=SE)", width=20, height=3,  # SE → south east
      bg="red", fg="white").pack(anchor=SE)


window.mainloop()
