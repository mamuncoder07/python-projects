import os

# Text to search
text = input("Enter text to search: ")

# Folder path
path = input("Enter folder path: ")

# Loop through files in folder
for file_name in os.listdir(path):
    file_path = os.path.join(path, file_name)

    # Check only files
    if os.path.isfile(file_path):
        try:
            with open(file_path, "r") as file:
                content = file.read()

                if text in content:
                    print("Text found in:", file_name)

        except:
            print("Could not read:", file_name)
