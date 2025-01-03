from tkinter import *

# 初始化Tk()
window = Tk()

window.title("Message Demo 2")

the_zen_of_python = "Beautiful is better than ugly." \
"Explicit is better than implicit." \
                    "Simple is better than complex."\
                    "Beautiful is better than ugly." \
                    "Explicit is better than implicit." \
                    "Simple is better than complex."\
                    "Beautiful is better than ugly." \
                    "Explicit is better than implicit." \
                    "Simple is better than complex."
msg = Message(window, text=the_zen_of_python, width=400)  # 在Msg里，width的单位是像素
msg.config(bg='CornflowerBlue', font=('Times', 20, 'italic'))
msg.pack()

window.mainloop()
