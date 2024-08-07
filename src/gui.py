from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QFrame,
)
from PyQt5.QtCore import Qt
from config import TITLE, WIDTH, HEIGHT, IMAGE_SIZES
from utils import open_folder, drop
import os
from image_processor import process_images





class DropFrame(QFrame):
    def __init__(self, parent=None):
        super(DropFrame, self).__init__(parent)
        self.setAcceptDrops(True)
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #f0f0f0;")  # Styling for visibility

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        folder_paths = [
            url.toLocalFile()
            for url in event.mimeData().urls()
            if os.path.isdir(url.toLocalFile())
        ]
        for folder_path in folder_paths:
            process_images(folder_path, IMAGE_SIZES)
            self.openFolder(os.path.join(folder_path, "resized"))

    def openFolder(self, path):
        import subprocess
        import sys

        if sys.platform == "darwin":
            subprocess.call(["open", path])
        elif sys.platform == "linux":
            subprocess.call(["xdg-open", path])
        else:
            os.startfile(path)


def create_main_window():

    # Create the main window & app.
    window = QMainWindow()

    # Set window attributes.
    window.setWindowTitle(TITLE)
    window.setMinimumSize(WIDTH, HEIGHT)

    # Central Widget, holds main layout.
    central_widget = QWidget(window)
    window.setCentralWidget(central_widget)

    main_layout = QHBoxLayout()

    # Column 1
    left_col_layout = QVBoxLayout()
    left_col_frame = QFrame()
    left_col_frame.setLayout(left_col_layout)
    left_col_label = QLabel("Drag a folder to the drop area or select a folder below.")
    left_col_button = QPushButton("Browse Folder")
    left_col_button.clicked.connect(open_folder)
    left_col_layout.addWidget(left_col_label)
    left_col_layout.addWidget(left_col_button)

    # Column 2
    right_col_layout = QVBoxLayout()
    right_col_frame = DropFrame()
    right_col_frame.setLayout(right_col_layout)
    right_col_label = QLabel("Drop folder here!")
    right_col_layout.addWidget(right_col_label)

    ## Add frames to the main layout with size ratio
    main_layout.addWidget(left_col_frame, 2)  # 40%
    main_layout.addWidget(right_col_frame, 3)  # 60%

    central_widget.setLayout(main_layout)

    return window
