from tkinter import *
from tkinter.messagebox import *
import webbrowser

window = Tk()
window.title("Magikid Login Window")
width = 300 # width of the window
height = 200 # height of the window

screenwidth = window.winfo_screenwidth() # grabs the actual width of your computer screen
screenheight = window.winfo_screenheight() # grabs the actual height of your computer screen
print(str(screenwidth) + "x" + str(screenheight))

alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2) # centers login screen on our pc screen
window.geometry(alignstr)

# %s means formatting an object as a string
# %d means formatting an object as an integer 
# Example:
# "Hello, %s" % "Stephanie" => "Hello, Stephanie"
# "Hello, I am %d years old" % "24" => "Hello, I am 24 years old"

username = StringVar()
password = StringVar()

def login_check(): # checks if login info is correct
    user = username.get()
    secret = password.get()
    if user == 'Magikid' and secret == '123456': # actual login info
        window.destroy()
        webbrowser.open("http://www.magikid.com")
    else:
        showinfo(title='mistake', message='Incorrect username or password!')
        print('Incorrect username or password!')

Label(window).grid(row=0, stick=W, pady=10) # 1st row, border width, padding

Label(window, text='account:').grid(row=1, stick=W, padx=20, pady=10) #2nd row, border width, horizontal padding, vertical padding
Entry(window, textvariable=username).grid(row=1, column=1, stick=E) # 2nd row, 2nd column, border width

Label(window, text='password:').grid(row=2, stick=W, padx=20, pady = 10)
Entry(window, textvariable=password, show="*").grid(row=2, column=1, stick=E)

Button(window, text='login', command=login_check).grid(row=3, stick=W, padx=20, pady=10)
Button(window, text='quit', command=window.quit).grid(row=3, column=1, stick=E)

window.mainloop()