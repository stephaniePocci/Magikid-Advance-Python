from tkinter import *

# Step1: Create a main window named 'window'
window = Tk()

# Step2: Set window title named 'My Window'
window.title('My Window')

# Step3: Set window size and position
window.geometry('400x300+1000+150')

# Step4: Create 'Entry' widgets
entry1 = Entry(window, show='*', font=('Arial', 16))  # Show in ciphertext
entry2 = Entry(window, show=None, font=('Arial', 16))  # Show in plaintext
entry3 = Entry(window, show=None, font=('Times', 18, 'bold italic'))
entry1.pack()
entry2.pack()
entry3.pack()

# Step5: Set the main window loop
window.mainloop()



