import tkinter as tk
import subprocess

def open_main_py():
    # This function will open mainAi.py in a separate process
    subprocess.Popen(["python", "mainAi.py"])
def multiplayer():
    # This function will open multiplayer.py in a separate process
    subprocess.Popen(["python", "multiplayer.py"])

# Function to change cursor to a hand pointer when hovering over the button
def change_to_pointer(event):
    button.config(cursor="hand2")

def change_to_arrow(event):
    button.config(cursor="arrow")

# Create the main window
root = tk.Tk()
root.title("Connect Four App")
root.configure(bg="#2e3d52")  # Set background color of main window

# Set the size of the main window
root.geometry("600x500")  # Set the width and height of the window

# Welcome message
welcome_label = tk.Label(root, text=" 🌟Connect Four Game🌟 ", font=("Helvetica", 30),width=100, fg="white", bg="#28ad62")
welcome_label.pack(pady=20)

# Team members
team_label = tk.Label(root, text="Team Members :", font=("Helvetica", 26), fg="white", bg="#2e3d52")
team_label.pack(pady=10)

# List of team members
team_members = ["Ahmed Wael Kamal ☻"]

for member in team_members:
    member_label = tk.Label(root, text=member, font=("Helvetica", 30), fg="white",  bg="#2e3d52")
    member_label.pack()

# Create a button
button = tk.Button(root, text="Single Player (With AI) ", command=open_main_py, width=25, height=1, bg="#28ad62", fg="white", font=("Helvetica", 24))
button.pack(pady=30)

# Create a button
button = tk.Button(root, text="Multi Player", command=multiplayer, width=25, height=1, bg="#28ad62", fg="white", font=("Helvetica", 24))
button.pack(pady=5)

# Bind events to change cursor when hovering over the button
button.bind("<Enter>", change_to_pointer)
button.bind("<Leave>", change_to_arrow)

# Run the main event loop
root.mainloop()
