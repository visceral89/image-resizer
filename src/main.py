from gui import create_main_window
import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD


def main():
    root = TkinterDnD.Tk()
    create_main_window(root)
    root.mainloop()


if __name__ == "__main__":
    main()
