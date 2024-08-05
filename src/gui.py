from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtCore import Qt
from config import TITLE, WIDTH, HEIGHT
from utils import open_folder, drop


def create_main_window():

    # Create the main window & app.
    app = QApplication([])
    window = QMainWindow()

    # Set window attributes.
    window.setWindowTitle(TITLE)
    window.setMinimumSize(WIDTH, HEIGHT)
    central_widget = QWidget()
    window.setCentralWidget(central_widget)

    layout = QVBoxLayout()

    

    drop_label = ttk.Label(root, text="Drop Folder Here", padding=10)
    drop_label.pack(expand=True, fill="both", padx=10, pady=10)

    or_label = ttk.Label(root, text="or", padding=10)
    or_label.pack(expand=True, fill="both", padx=10, pady=10)

    button = ttk.Button(root, text="Browse Folder", command=open_folder)
    button.pack(pady=20)

    root.drop_target_register(DND_FILES)
    root.dnd_bind("<<Drop>>", drop)
