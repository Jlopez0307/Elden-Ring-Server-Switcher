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

def resize_image(event):
    new_width = event.width
    new_height = event.height

    resized_image = original_image.resize((new_width, new_height), Image.ANTIALIAS)
    new_bg_photo = ImageTk.PhotoImage(resized_image)

    canvas.itemconfig(bg_image_id, image=new_bg_photo)
    canvas.image = new_bg_photo

    canvas.tag_raise(header_label_window)
    canvas.tag_raise(rename_button_window)
    canvas.tag_raise(start_button_window)

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
image_path = "./images/ersc_wallpaper.jpg"
original_image = Image.open(image_path)

# Original image size
original_width, original_height = original_image.size

# Create the main application window
app = tk.Tk()
app.title("Elden Ring Seamless Co-Op Server Switcher")
app.geometry(f"{original_width}x{original_height}")

app.minsize(original_width, original_height)


# Canvas for background image
canvas = tk.Canvas(app, width=original_width, height=original_height)
canvas.pack(fill="both", expand=True)

initial_bg_photo = ImageTk.PhotoImage(original_image)
bg_image_id = canvas.create_image(0, 0, image=initial_bg_photo, anchor="nw")

# # Frame to hold widgets on top of canvas
# frame = tk.Frame(app)
# frame.place(relx=0.5, rely=0.5, anchor="center")


# Create and pack the header label
header_label = tk.Label(
    app,
    text=f"Current Filename: {check_current_filename()}",
    font=("Helvetica", 25, "bold"),
    fg="#D8DEE9",
    bg="#2E3440"
)
header_label_window = canvas.create_window(original_width//2, 50, window=header_label)

rename_button = tk.Button(
    app,
    text="Switch Servers",
    command=rename_file,
    font=("Helvetica", 14),
    bg="#4C566A",
    fg="#D8DEE9",
    activebackground="#5E81AC",
    activeforeground="#ECEFF4",
    relief=tk.RAISED,
    bd=3,
)
rename_button_window = canvas.create_window(original_width//2, 200, window=rename_button)

start_button = tk.Button(
    app,
    text="Start ER:SC",
    command=start_ersc,
    font=("Helvetica", 14),
    bg="#4C566A",
    fg="#D8DEE9",
    activebackground="#5E81AC",
    activeforeground="#ECEFF4",
    relief=tk.RAISED,
    bd=3,
)
start_button_window = canvas.create_window(original_width//2, 250, window=start_button)


# # Create and pack the rename button
# rename_button = tk.Button(frame, text="Switch Servers", command=rename_file)
# rename_button.pack(side=tk.LEFT, padx=5)

# # Create and pack the run button
# run_button = tk.Button(frame, text="Start", command=start_ersc)
# run_button.pack(side=tk.RIGHT, padx=5)

app.update_idletasks()

# Check filename at launch
update_header()

app.bind("<Configure>", resize_image)

# Run the main loop
app.mainloop()


        