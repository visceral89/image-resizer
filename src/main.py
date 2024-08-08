from gui import create_main_window
from PyQt5.QtWidgets import QApplication


def load_stylesheet(path):
    with open(path, "r") as f:
        return f.read()


def main():
    app = QApplication([])
    # stylesheet = load_stylesheet("styles.qss")
    # app.setStyleSheet(stylesheet)
    window = create_main_window()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
