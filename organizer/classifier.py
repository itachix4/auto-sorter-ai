import os
import shutil
from organizer.file_rules import FILE_RULES

def move_file(file_path, downloads_path):
    _, ext = os.path.splitext(file_path)
    
    for folder, extensions in FILE_RULES.items():
        if ext.lower() in extensions:
            target_folder = os.path.join(downloads_path, folder)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, target_folder)
            return f"Moved {file_path} → {folder}"

    return f"No rule for {file_path}, leaving it."
