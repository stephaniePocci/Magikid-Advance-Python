from tkinter import *
from tkinter.messagebox import *
import webbrowser
# webbrowser is a library that comes with python3

"""import webbrowser as web"""

window = Tk()
window.title("Login Window")
width = 300
height = 200

'''Get the width and height of the computer screen'''
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
print(str(screenwidth) + "x" + str(screenheight))

'''alignstr '''
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
window.geometry(alignstr)  # center alignment

'''
%s, means formatting an object as characters
%d, means formatting an object as an integer (decimal)

%, marks the beginning of the conversion specifier
Place a string (the format string) on the left side of %
and the value you want to format on the right side.

Example：
"Hello, %s" % "zhang3" => "Hello, zhang3"
"%d" % 33 => "33"
"%s:%d" % ("ab",3) => "ab:3"
'''

username = StringVar()
password = StringVar()


def login_check():
    name = username.get()
    secret = password.get()
    if name == 'Magikid' and secret == '123456':
        window.destroy()
        webbrowser.open("http://www.magikid.com")
    else:
        showinfo(title='mistake', message='Incorrect username or password！')
        print('Incorrect username or password！')


Label(window).grid(row=0, stick=W, pady=10)

Label(window, text='account:').grid(row=1, stick=W, padx=20, pady=10)
Entry(window, textvariable=username).grid(row=1, column=1, stick=E)

Label(window, text='password:').grid(row=2, stick=W, padx=20, pady=10)
Entry(window, textvariable=password, show='*').grid(row=2, column=1, stick=E)

Button(window, text='login', command=login_check).grid(row=3, stick=W, padx=20, pady=10)
Button(window, text='quit', command=window.quit).grid(row=3, column=1, stick=E)

window.mainloop()
