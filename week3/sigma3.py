from tkinter import *

window = Tk()

window.geometry("500x500+2000+100")

# Side: LEFT, RIGHT, BOTTOM, TOP
# Anchor: N, NE, E, SE, S, SW, W, NW. CENTER
Label(window, text="Hello").pack(anchor=NE)

display = StringVar()

display.set("NO CLICKS")

i = 0
def increment():
    global i
    i += 1
    display.set("Clicks: " + str(i))


Label(window, textvariable=display, font=("Arial", 20), bg="black", fg="white").pack()

Button(window, text="tap", command=increment).pack()

window.mainloop()




# +1 to have a custom title
# +1 to have a label as a heading
# +1 to move the button to the bottom right
# +1 to move the score tally to the bottom left
# +1 change the button text when clicked
# +3 add your own twist 



