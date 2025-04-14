import os
import shutil

# Define the file type categories and their corresponding folders
FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav", ".aac"],
    "Pictures": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Presentations": [".ppt", ".pptx"],
    "Scripts": [".py", ".js", ".sh", ".bat"]
}

def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False

            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    category_path = os.path.join(directory, category)
                    os.makedirs(category_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_path, filename))
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(directory, "Others")
                os.makedirs(other_path, exist_ok=True)
                shutil.move(file_path, os.path.join(other_path, filename))

if __name__ == "__main__":
    target_directory = input("Enter the path to the directory you want to organize: ")
    if os.path.exists(target_directory):
        organize_files(target_directory)
        print("Files organized successfully.")
    else:
        print("The provided path does not exist.")
