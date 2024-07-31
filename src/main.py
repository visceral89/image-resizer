from gui import create_main_window
import customtkinter as ctk


def main():
    root = ctk.CTk()
    create_main_window(root)
    root.mainloop()


if __name__ == "__main__":
    main()
