import tkinter as tk
import random

class ColorMatchingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Matching Challenge")

        # Target and player colors
        self.target_color = [0, 0, 0]
        self.player_color = [0, 0, 0]

        # Labels
        tk.Label(root, text="Match the Target Color!", font=("Helvetica", 14)).pack(pady=10)

        # Canvas to display colors
        self.canvas = tk.Canvas(root, width=300, height=100, bg="white")
        self.canvas.pack(pady=10)

        # Draw the target and player color rectangles
        self.target_rect = self.canvas.create_rectangle(20, 20, 140, 80, fill="black", outline="black")
        self.player_rect = self.canvas.create_rectangle(160, 20, 280, 80, fill="black", outline="black")

        # Label for checkboxes
        tk.Label(root, text="Toggle the colors to match the target:", font=("Helvetica", 12)).pack(pady=5)

        # Variables for checkboxes
        self.checkbox_vars = [tk.IntVar() for _ in range(3)]

        # Checkboxes for Red, Green, Blue
        self.colors = ["Red", "Green", "Blue"]
        for i, color in enumerate(self.colors):
            cb = tk.Checkbutton(root, text=color, variable=self.checkbox_vars[i], fg=color.lower(),
                                 command=self.update_player_color)
            cb.pack(anchor="w", padx=20)

        # Submit button
        self.submit_button = tk.Button(root, text="Submit", command=self.check_match)
        self.submit_button.pack(pady=10)

        # Feedback label
        self.feedback_label = tk.Label(root, text="", font=("Helvetica", 10), fg="blue")
        self.feedback_label.pack()

        # Generate target color
        self.generate_target_color()

    def generate_target_color(self):
        # Randomly set target color
        self.target_color = [random.choice([0, 255]) for _ in range(3)]
        target_hex = self.rgb_to_hex(self.target_color)
        self.canvas.itemconfig(self.target_rect, fill=target_hex)
        self.update_player_color()  # Initialize player color

    def update_player_color(self):
        # Update player color based on checkbox states
        self.player_color = [255 if var.get() else 0 for var in self.checkbox_vars]
        player_hex = self.rgb_to_hex(self.player_color)
        self.canvas.itemconfig(self.player_rect, fill=player_hex)

    def check_match(self):
        # Check if player color matches target color
        if self.player_color == self.target_color:
            self.feedback_label.config(text="Correct! You matched the color!", fg="green")
            self.submit_button.config(state=tk.DISABLED)  # Disable button after success
        else:
            self.feedback_label.config(text="Not a match! Try again!", fg="red")

    @staticmethod
    def rgb_to_hex(rgb):
        # Convert RGB list to hex color string
        return "#{:02x}{:02x}{:02x}".format(*rgb)

# Create the GUI window
root = tk.Tk()
game = ColorMatchingGame(root)
root.mainloop()
