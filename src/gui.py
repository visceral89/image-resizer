from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
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
            subprocess.call(["xdg-open"], path)
        else:
            os.startfile(path)


def create_main_window():

    # Create the main window & app.
    window = QMainWindow()

    # Set window attributes.
    window.setWindowTitle(TITLE)
    window.setMinimumSize(WIDTH, HEIGHT)
    central_widget = QWidget()
    window.setCentralWidget(central_widget)

    main_layout = QVBoxLayout()

    # Content Frame
    content_frame = QFrame()
    content_layout = QVBoxLayout(content_frame)
    instructions_label = QLabel(
        "Drag a folder to the drop area or select a folder below."
    )
    instructions_label.setAlignment(Qt.AlignCenter)
    content_layout.addWidget(instructions_label)

    browse_button = QPushButton("Browse Folder")
    browse_button.clicked.connect(lambda: print("Browse Folder Clicked"))
    content_layout.addWidget(browse_button)

    # Drop Frame
    drag_frame = DropFrame()
    main_layout.addWidget(drag_frame, 3)

    ## Add frames to the main layout with size ratio
    main_layout.addWidget(content_frame, 2)  # 40%
    main_layout.addWidget(drag_frame, 3)  # 60%

    central_widget.setLayout(main_layout)

    return window
