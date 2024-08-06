from gui import create_main_window
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication([])
    window = create_main_window()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
