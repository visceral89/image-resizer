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

    main_layout = QVBoxLayout()

    ## Start new Design

    # Header
    text_area = QVBoxLayout()
    title_text = QLabel("Welcome to emote and image resizer")
    title_text.setAlignment(Qt.AlignCenter)
    subtitle_text = QLabel(
        "Upload folder with files. The resizer supports .png, .jpg, .jpeg and .gif"
    )
    subtitle_text.setAlignment(Qt.AlignCenter)

    main_layout.addWidget(title_text)
    main_layout.addWidget(subtitle_text)

    # Drag and Drop Area
    drag_frame = DropFrame()
    drag_frame.setFrameShape(QFrame.StyledPanel)
    drag_frame.setFrameShadow(QFrame.Raised)
    drag_frame.setStyleSheet("border: 2px dashed #ccc;")

    drag_layout = QVBoxLayout()
    drag_label = QLabel("Drag and Drop Folder here")
    drag_label.setAlignment(Qt.AlignCenter)

    browse_button = QPushButton("Browse Folder")
    browse_button.setStyleSheet("background-color: #dad7cd; color: white;")
    drag_layout.addWidget(drag_label)
    drag_layout.addWidget(browse_button)
    drag_frame.setLayout(drag_layout)

    main_layout.addWidget(drag_frame)

    central_widget.setLayout(main_layout)

    return window
