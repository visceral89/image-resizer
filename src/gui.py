from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD
from config import TITLE, WINMINSIZE
from utils import open_folder


def create_main_window(root):
    root.title(TITLE)
    root.geometry(WINMINSIZE)

    style = ttk.Style()
    style.theme_use("alt")

    label = ttk.Label(root, text="Drop Folder Here", padding=10)
    label.pack(expand=True, fill="both", padx=10, pady=10)
    label = ttk.Label(root, text="or", padding=10)
    label.pack(expand=True, fill="both", padx=10, pady=10)

    button = ttk.Button(root, text="Browse Folder", command=open_folder)
    button.pack(pady=20)

    root.drop_target_register(DND_FILES)
    root.dnd_bind("<<Drop>>", lambda event: on_drop(event, label, root))


def on_drop(event, label, root):
    files = root.tk.splitlist(event.data)
    label["text"] = "\n".join(f for f in files)
