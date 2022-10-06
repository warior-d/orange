import os

with os.scandir(os.getcwd()) as files:
    for file in files:
        if file.is_file():
            print(file)