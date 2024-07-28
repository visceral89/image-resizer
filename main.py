import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
import os

sizes = [28, 56, 112, 512]

# 28, 56, 112, 512


def resize_images(folder_path, output_sizes):
    output_folder = os.path.join(folder_path, "resized")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(folder_path):
        if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
            image_path = os.path.join(folder_path, file)
            img = Image.open(image_path)

            for size in output_sizes:
                resized_img = img.resize((size, size))
                resized_img.save(os.path.join(output_folder, f"{size}px_{file}"))


def open_folder():
    initial_directory = os.path.expanduser("~/Pictures")
    folder_selected = filedialog.askdirectory(initialdir=initial_directory)
    if folder_selected:
        resize_images(folder_selected, sizes)
        label.config(text=f"Images resized in {folder_selected}/resized")


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")


# APP SETUP
app = ctk.CTk()
app.title("Jessicas Batcher")
app.geometry("400x300")
app.minsize(400, 300)
app.maxsize(1920, 1080)

# MAIN FRAME

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Select a folder", font=("Inter", 24))
label.pack(pady=20)

button = ctk.CTkButton(master=frame, text="Select Folder", command=open_folder)
button.pack(pady=10)

app.mainloop()
