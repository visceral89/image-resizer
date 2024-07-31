import os
from tkinter import filedialog
from image_processor import process_images
from config import IMAGE_SIZES


def drop(event):
    folder_path = event.data.replace("{", "").replace("}", "")
    if os.path.isdir(folder_path):
        process_images(folder_path, IMAGE_SIZES)
        os.startfile(os.path.join(folder_path, "resized"))


def open_folder():
    initial_directory = os.path.expanduser("~/Pictures")
    folder_selected = filedialog.askdirectory(initialdir=initial_directory)
    if folder_selected:
        process_images(folder_selected, IMAGE_SIZES)
