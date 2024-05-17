import tkinter as tk
import subprocess
import os

def resize_font(event):
    new_size = max(20, min(event.width // 10, event.height // 6))  # Adjust the font size relative to the window size
    label.config(font=("Bell MT", new_size, "bold"))

# Function to be executed on button click
def on_button_click():
    print("Let's Go button clicked!")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    subprocess.Popen(["python", os.path.join(current_dir, "3.py")])  # Execute 3.py file

# Create the main application
root = tk.Tk()
root.title("Pixel Harbour")

# Set the background color of the window
root.configure(bg='#f0f0f0')

# Disable the window size propagation
root.pack_propagate(0)

# Calculate the center coordinates of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 400
window_height = 300
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the geometry of the window to open in the center
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a label with the welcome message and defined font parameters
label = tk.Label(root, text="Welcome to Pixel Harbour", font=("Bell MT", 32, "bold"), bg='#f0f0f0')
label.place(relx=0.5, rely=0.4, anchor="center")

# Create the "Let's Go" button with adjusted padding
button = tk.Button(root, text="Let's Go", font=("Cambria", 18,), command=on_button_click, padx=1, pady=1)
button.place(relx=0.5, rely=0.6, anchor="center")

# Bind the label to the window resize event
root.bind("<Configure>", resize_font)

# Run the application
root.mainloop()
