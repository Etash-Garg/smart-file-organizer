import os
import shutil
print("Enter the folder path:")
folder_path = input("")
if not os.path.isdir(folder_path):
    print("Invalid folder path.")
    exit()
extension_map={
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".mp3": "Audio",
    ".wav": "Audio"
}
counts = {}
files = os.listdir(folder_path)
files_checked = 0
for file in files:                                              #file scanning
    full_path = os.path.join(folder_path, file)
    if os.path.isfile(full_path):                               #check if file
        files_checked +=1
        extension = os.path.splitext(file)[1].lower()
        category = extension_map.get(extension, "Other")
        counts[category] = counts.get(category, 0) + 1
        category_path = os.path.join(folder_path, category)
        destination_path = os.path.join(category_path, file)
        if not os.path.exists(category_path):
            os.mkdir(category_path)                             #folder creation
        counter = 1
        while os.path.exists(destination_path):
            name, ext = os.path.splitext(file)
            new_name = f"{name}_{counter}{ext}"
            destination_path = os.path.join(category_path, new_name)
            counter += 1
        shutil.move(full_path, destination_path)                #moving files
print(f"Total files checked: {files_checked}")
for category in sorted(counts):
     print(f"Total files in {category} folder: {counts[category]}")