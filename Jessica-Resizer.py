from tkinterdnd2 import DND_FILES, TkinterDnD
import customtkinter as ctk
from tkinter import filedialog, StringVar, TOP
from PIL import Image
import os

sizes = [28, 56, 112, 512]


class Tk(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")


# 28, 56, 112, 512
# Fix filenames to {file}@{size}px"
# Todo: Make draggable folder in window, run resize_images function
# Open Folder on Complete


def drop(event):
    folder_path = event.data
    if os.path.isdir(folder_path):
        resize_images(folder_path, sizes)
        label.config(text=f"Images resized in {folder_path}/resized")
        os.startfile(os.path.join(folder_path, "resized"))


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
                resized_img.save(os.path.join(output_folder, f"{size}px-{file}"))
    os.startfile(os.path.join(output_folder))


def open_folder():
    initial_directory = os.path.expanduser("~/Pictures")
    folder_selected = filedialog.askdirectory(initialdir=initial_directory)
    if folder_selected:
        resize_images(folder_selected, sizes)
        label.config(text=f"Images resized in {folder_selected}/resized")


# APP SETUP
root = Tk()
root.title("Jessica Resizer")
root.geometry("400x300")
root.minsize(400, 300)
root.maxsize(1920, 1080)

# MAIN FRAME

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
frame.drop_target_register(DND_FILES)
frame.dnd_bind("<<Drop>>", drop)

label = ctk.CTkLabel(master=frame, text="Drag Folder Here", font=("Inter", 32))
label.pack(pady=20)

button = ctk.CTkButton(master=frame, text="Select Folder", command=open_folder)
button.pack(pady=50)

root.mainloop()
