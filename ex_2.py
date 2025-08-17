#!/usr/bin/env python3
import os

def create_new_dir(name_dir: str):
    corrent_path = os.getcwd()
    print(corrent_path)
    path_dir = os.path.join(corrent_path, name_dir)
    if not os.path.isdir(path_dir):
        os.mkdir(path_dir)
    file_path = os.path.join(path_dir, "hello.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Hello from Python")
        
    return file_path

def checked_file_and_read(file_path: str):
    if os.access(file_path, os.F_OK) | os.R_OK:
        with open(file_path, "r") as f:
            print(f.read())


if __name__ == "__main__":
    
    file = create_new_dir("test_dir")
    checked_file_and_read(file)
    