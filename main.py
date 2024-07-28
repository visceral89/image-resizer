import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

size1 = 28,28
size2 = 56,56
size3 = 112,112
size4 = 512,512

# 28, 56, 112, 512

def resize_images(dir, output_size=(512,512));
    for file in os.listdir(dir):
        if file.lower().endswith((".png",".jpg", ".jpeg", ".gif")):
            image_path = os.path.join(dir,file)
            img = Image.open(image_path)
            img = img.resize(output_size, Image.ANTIALIAS)
            img.save(os.path.join(dir, f"{file}{output_size}"))
