"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Rivera, Renz Lui B.]
Date: [9/27/26]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[So basically as it's named it is a file sorting program where it checks for the file extension and moves it to a folder with it's proper label
like for example when you create a mp4 file, once you run the program it will ask for the directory or you can keep the current directory to use, anyways 
it will scan or check every file's extension name like mp4, mp3, png and so on and then put it inside a folder where it belongs, to do that you must first 
create a dictionary with every types of extensions you know as you can see down there in my categories dictionary, next is like i mentioned earlier it will
ask for a directory to sort or organize or you can just press enter to sort the current directory, then once the directory is set or declared it will check 
if that directory exist as you can see down there, if it does not exist it will display an error message, but if it does exist it will proceed, then there 
comes the file scanning, it will check the extensions inside the declared directory and then checks what category it matches, if there's no folder created 
inside that directory that matches the file, it will create one for that file to move it inside, but if there's a file that doesn't match any of the extensions
declared inside the dictionary it will create a "Others" folder and move it there, I also forgot to mention that it will ignore files without extensions, that's
pretty much it for this program]


============================================
KEY VOCABULARY
============================================
- os module:
- shutil module:
- file path:
- directory:
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

# Dictionary mapping folder names to file extensions
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".flac", ".m4a"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".html", ".css", ".js", ".json", ".cpp"]
}

def sort_files(target_dir="."):
    # Resolve absolute path to avoid directory trajectory errors
    abs_target_dir = os.path.abspath(target_dir)

    if not os.path.exists(abs_target_dir) or not os.path.isdir(abs_target_dir):
        print(f"Error: Directory '{abs_target_dir}' does not exist.")
        return

    moved_count = 0

    # Scan items in the target directory
    for item in os.listdir(abs_target_dir):
        item_path = os.path.join(abs_target_dir, item)

        # Skip subdirectories
        if os.path.isdir(item_path):
            continue

        filename, extension = os.path.splitext(item)
        extension = extension.lower()

        # Skip files with no extension
        if not extension:
            continue

        # Find matching category
        target_category = "Others"
        for category, ext_list in CATEGORIES.items():
            if extension in ext_list:
                target_category = category
                break

        # Create destination folder if it doesn't exist
        dest_folder = os.path.join(abs_target_dir, target_category)
        os.makedirs(dest_folder, exist_ok=True)

        # Target file location
        dest_path = os.path.join(dest_folder, item)

        # Prevent overwriting existing files with duplicate names
        if os.path.exists(dest_path):
            dest_path = os.path.join(dest_folder, f"{filename}_copy{extension}")

        # Move the file
        shutil.move(item_path, dest_path)
        print(f"Moved: '{item}' -> '{target_category}/'")
        moved_count += 1

    print(f"\nSorting complete! Successfully organized {moved_count} file(s).")


if __name__ == "__main__":
    folder_input = input("Enter folder path to organize (press Enter for current directory): ").strip()
    sort_files(folder_input if folder_input else ".")
# --- paste your existing code here ---


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[my mistake here was not making a category checker or a category dictionary to check where the file needs to go since i thought it will 
automatically know]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
