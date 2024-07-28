import tkinter as tk
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
                resized_img = img.resize((size, size), Image.ANTIALIAS)
                resized_img.save(os.path.join(output_folder, f"{size}px_{file}"))


def open_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        resize_images(folder_selected, sizes)
        label.config(text=f"Images resized in {folder_selected}/resized")


app = tk.Tk()
app.title("Jessicas Batcher")

label = tk.Label(app, text="Select a folder to resize images")
label.pack(pady=20)

button = tk.Button(app, text="Select Folder", command=open_folder)
button.pack(pady=10)

app.mainloop()
