from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD
from config import TITLE, WINMINSIZE


def create_main_window(root):
    root.title(TITLE)
    root.geometry(WINMINSIZE)

    style = ttk.Style()
    style.theme_use("alt")

    label = ttk.Label(root, text="Drop Folder Here", padding=10)
    label.pack(expand=True, fill="both", padx=10, pady=10)

    root.drop_target_register(DND_FILES)
    root.dnd_bind("<<Drop>>", lambda event: on_drop(event, label))
