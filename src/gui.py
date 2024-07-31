from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD
from config import TITLE, WINMINSIZE
from utils import open_folder, drop  # Make sure to import the drop function


def create_main_window(root):
    root.title(TITLE)
    root.geometry(WINMINSIZE)

    style = ttk.Style()
    style.theme_use("alt")

    drop_label = ttk.Label(root, text="Drop Folder Here", padding=10)
    drop_label.pack(expand=True, fill="both", padx=10, pady=10)

    or_label = ttk.Label(root, text="or", padding=10)
    or_label.pack(expand=True, fill="both", padx=10, pady=10)

    button = ttk.Button(root, text="Browse Folder", command=open_folder)
    button.pack(pady=20)

    root.drop_target_register(DND_FILES)
    root.dnd_bind("<<Drop>>", drop)  # Using the drop function from utils directly


# Update the drop function in utils.py to handle GUI feedback, e.g., updating the drop_label text.
