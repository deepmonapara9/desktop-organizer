# Desktop Screenshot Organizer

## Project Description

**Desktop Screenshot Organizer** is a Python project that helps you automatically organize all screenshots on your desktop. The script finds screenshot files based on their extensions and moves them into a "Screenshots" folder located on your desktop. This makes it easy to keep your desktop tidy and organized.

## Features

- Automatically finds all screenshots on your desktop.
- Moves screenshots into a "Screenshots" folder.
- Organizes files based on their extension (e.g., `.png`, `.jpg`, `.jpeg`).

## Requirements

To run this project, you need the following:

- Python 3.x (comes with `os` and `shutil` modules pre-installed)

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/deepmonapara9/desktop-organizer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd desktop-screenshot-organizer
    ```

3. Run the script:

    ```bash
    python organize_screenshots.py
    ```

## Usage

1. Place the `organize_screenshots.py` script on your desktop or in a directory where you want to organize your screenshots.
2. Run the script using Python. It will:
   - Create a "Screenshots" folder on your desktop (if it doesn't already exist).
   - Move all screenshot files (`.png`, `.jpg`, `.jpeg`, etc.) into the "Screenshots" folder.

## How It Works

1. The script searches the desktop for files with common screenshot extensions (e.g., `.png`, `.jpg`, `.jpeg`).
2. It checks if the "Screenshots" folder exists on the desktop. If not, it creates one.
3. It moves the matching files to the "Screenshots" folder.
