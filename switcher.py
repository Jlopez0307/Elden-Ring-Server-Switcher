#!/usr/bin/env python3
import os
import sys
import subprocess
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def check_current_filename():
    current_directory_files = os.listdir()
    if original_server in current_directory_files:
        return original_server
    elif spacewar_server in current_directory_files:
        return spacewar_server
    else:
        return None
    
def update_header():
    existing_file = check_current_filename()
    if existing_file == original_server:
        header_label.config(text=f"Current Server: Spacewar")
    elif existing_file == spacewar_server:
        header_label.config(text=f"Current Serer: Original Server")
    else:
        header_label.config(text="No relevant files found in the directory")


def rename_file():
    existing_file = check_current_filename()
    if existing_file == original_server:
        try:
            os.rename(original_server, spacewar_server)
            messagebox.showinfo("Success", f"Server Switched to Original Server")
            update_header()
        except OSError as e:
            messagebox.showerror("Error", f"Error renaming file: {e}")
    elif existing_file == spacewar_server:
        # Prompt user to switch from Spacewar server
        try:
            os.rename(spacewar_server, original_server)
            messagebox.showinfo("Success", f"Server switched to Spacewar")
            update_header()
        except OSError as e:
            messagebox.showinfo("Error", f"Error siwtching servers: {e}")
    else: 
        messagebox.showinfo(f"Server switch not possible. Cant find '{original_server}' or '{spacewar_server} in current directory")

def start_ersc():
    try:
        subprocess.run(['./ersc_launcher.exe'])
        app.destroy()
    except Exception as e:
        messagebox.showinfo(f"Error executing another script: {e}")


#Initializing variables
original_server = "winmm.dll"
spacewar_server = "winmm.dll.bak"

# Load the background image
# bg_image = Image.open("RckaTm0.png")


# Create the main application window
app = tk.Tk()
app.title("Elden Ring Seamless Co-Op Server Switcher")
app.geometry("400x300")

# Load the background image
image_path = "background.png"
bg_image = Image.open('./RckaTm0.png')
bg_image = bg_image.resize((500,800), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Canvas for background image
canvas = tk.Canvas(app, width=400, height=300)
canvas.pack(fill="both", expand=True)

# Set background image on canvas
canvas.create_image(0,0,image=bg_photo, anchor="nw")


# Frame to hold widgets on top of canvas
frame = tk.Frame(app)
frame.place(relx=0.5, rely=0.5, anchor="center")


# Create and pack the header label
header_label = tk.Label(app, text="", font=("Helvetica", 14))
header_label.pack(padx=10, pady=10)


# Create and pack the rename button
rename_button = tk.Button(frame, text="Switch Servers", command=rename_file)
rename_button.pack(side=tk.LEFT, padx=5)

# Create and pack the run button
run_button = tk.Button(frame, text="Start", command=start_ersc)
run_button.pack(side=tk.RIGHT, padx=5)

# Check filename at launch
update_header()

# Run the main loop
app.mainloop()


        