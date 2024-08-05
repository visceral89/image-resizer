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
from config import TITLE, WIDTH, HEIGHT
from utils import open_folder, drop

class DropLabel()


def create_main_window():

    # Create the main window & app.
    app = QApplication([])
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
    drag_frame = QFrame()
    drag_layout = QVBoxLayout(drag_frame)
    drop_label = QLabel("Drop Files Here")
    drop_label.setAlignment(Qt.AlignCenter)
    drop_label.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
    drop_label.setAcceptDrops(True)
    drop_label.setMinimumHeight(200)  # Adjust size
    drag_layout.addWidget(drop_label)

    ## Add frames to the main layout with size ratio
    main_layout.addWidget(content_frame, 2)  # 40%
    main_layout.addWidget(drag_frame, 3)  # 60%

    central_widget.setLayout(main_layout)

    window.show()
    app.exec_()
