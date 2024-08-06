# Image Resizer Tool

## Overview

This Image Resizer Tool is a desktop application designed to help users quickly resize images to multiple predefined dimensions. It supports various formats including JPG, PNG, and GIF (including animated GIFs). The application offers a simple drag-and-drop interface for ease of use.

## Features

- **Multiple Size Outputs**: Automatically resizes images to 28px, 56px, 112px, and 512px.
- **Drag-and-Drop Functionality**: Users can drag and drop a folder directly onto the application window.
- **Output Folder**: Automatically saves resized images in a subfolder called 'resized' within the original folder.
- **Custom Naming Convention**: Resized images are saved with their size appended to the filename (e.g., `filename@size.png`).
- **Support for Animated GIFs**: Properly handles resizing of animated GIFs by processing each frame to maintain the animation.

## Installation

### Prerequisites

- Python 3.12
- Pillow library
- PyQt5 5.15.11

### Usage

1. Run the script:

```bash
python main.py
```

2. Use the GUI to drag and drop a folder onto the window or use the 'Browse Folder' button to choose a folder.
3. Resized images will be saved in a 'resized' subfolder within the original folder. Each file will be named according to the format filename@size.extension.
