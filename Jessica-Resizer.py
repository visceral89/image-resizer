import os
import sys

# Add the path to the tkdnd library
tkdnd_library_path = "./tkdnd"
if getattr(sys, "frozen", False):
    # If running in a PyInstaller bundle
    base_path = sys._MEIPASS
    tkdnd_library_path = os.path.join(base_path, "tkdnd")

os.environ["TKDND_LIBRARY"] = tkdnd_library_path

from tkinterdnd2 import DND_FILES, TkinterDnD
import tkdnd
import customtkinter as ctk
from tkinter import filedialog, StringVar, TOP
from PIL import Image, ImageSequence


sizes = [28, 56, 112, 512]
extentions = [".png", ".jpg", ".jpeg", ".gif"]


class Tk(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")


# 28, 56, 112, 512
# installer command  "pyinstaller --onefile --windowed --add-data "C:\Python312\Lib\site-packages\tkdnd;./tkdnd" --icon=picture.ico Jessica-Resizer.py"


def drop(event):
    folder_path = event.data.replace("{", "").replace("}", "")
    if os.path.isdir(folder_path):
        resize_images(folder_path, sizes)
        label.configure(text=f"Images resized in {folder_path}/resized")
        os.startfile(os.path.join(folder_path, "resized"))


def resize_images(folder_path, output_sizes):
    output_folder = os.path.join(folder_path, "resized")
    # Make sure the folder excist, otherwise create it.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(folder_path):
        file_name, file_ext = os.path.splitext(file)
        if file_ext.lower() in extentions:
            image_path = os.path.join(folder_path, file)
            if file_ext.lower() == ".gif":
                for size in output_sizes:
                    output_path = os.path.join(
                        output_folder, f"{file_name}@{size}{file_ext}"
                    )
                    resize_gif(image_path, output_path, size)
            else:
                img = Image.open(image_path)
                for size in output_sizes:
                    resized_img = img.resize((size, size))
                    resized_img.save(
                        os.path.join(output_folder, f"{file_name}@{size}{file_ext}")
                    )

    os.startfile(os.path.join(output_folder))


def open_folder():
    initial_directory = os.path.expanduser("~/Pictures")
    folder_selected = filedialog.askdirectory(initialdir=initial_directory)
    if folder_selected:
        resize_images(folder_selected, sizes)
        label.configure(text=f"Images resized in {folder_selected}/resized")


def resize_gif(image_path, output_path, size):
    img = Image.open(image_path)
    frames = []

    for frame in ImageSequence.Iterator(img):
        frame = frame.convert("RGBA")
        resized_frame = frame.resize((size, size))
        frames.append(resized_frame)

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:1],
        optimize=False,
        loop=1,
        duration=img.info["duration"],
    )


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
