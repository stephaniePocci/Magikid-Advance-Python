import tkinter as tk

# Function to execute on button click
def on_button_click():
    print("Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Button Click Example")
root.geometry("200x100")

# Create a button and assign the command
button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack(pady=20)

# Run the application
root.mainloop()
