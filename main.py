import os
import shutil
from datetime import datetime

def organize_desktop():
    desktop_path = os.path.expanduser("~/Desktop")
    
    # Create folders for different file types
    folders = {
        "Images": [".png", ".jpg", ".jpeg", ".gif"],
        "Documents": [".pdf", ".doc", ".docx", ".txt"],
        "Screenshots": ["screenshot", "Screenshot"],
        "Others": []
    }
    
    for folder in folders:
        folder_path = os.path.join(desktop_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Organize files
    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)
        
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            
            # Check if it's a screenshot
            if any(s.lower() in filename.lower() for s in folders["Screenshots"]):
                destination = os.path.join(desktop_path, "Screenshots", filename)
            else:
                # Find the appropriate folder based on extension
                destination_folder = next(
                    (folder for folder, extensions in folders.items() if file_ext in extensions),
                    "Others"
                )
                destination = os.path.join(desktop_path, destination_folder, filename)
            
            # Move the file
            shutil.move(file_path, destination)
    
    print("Desktop organized successfully!")

if __name__ == "__main__":
    organize_desktop()
