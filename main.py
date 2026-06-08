import os
print("Enter the folder path:")
folder_path = input("")
files = os.listdir(folder_path)
for file in files:
    if os.path.isfile(os.path.join(folder_path, file)):
        print(file)