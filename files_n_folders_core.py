import os

def generate_folders(folders):
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

def generate_files(files):
    for file in files:
        with open(file, 'w') as f:
            pass  # This will create an empty file. Content will be added later.

def generate_file_contents(file_contents):
    for file_path, contents in file_contents.items():
        with open(file_path, 'w') as f:
            f.writelines(contents)

def generate_template(folders=None, files=None, file_contents=None):
    if folders:
        generate_folders(folders)
    if files:
        generate_files(files)
    if file_contents:
        generate_file_contents(file_contents)
