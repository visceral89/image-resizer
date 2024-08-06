import os
from image_processor import process_images
from config import IMAGE_SIZES
from PyQt5.QtWidgets import QFileDialog


def drop(event):
    folder_path = event.data.replace("{", "").replace("}", "")
    if os.path.isdir(folder_path):
        process_images(folder_path, IMAGE_SIZES)
        os.startfile(os.path.join(folder_path, "resized"))


def open_folder():
    initial_directory = os.path.expanduser("~/Pictures")
    folder_selected, _ = QFileDialog.getExistingDirectory(
        None, "Select Folder", initial_directory
    )
    if folder_selected:
        process_images(folder_selected, IMAGE_SIZES)
