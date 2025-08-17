#!/usr/bin/env python3
import os




def get_corrent_path() -> str:
    
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        BASE_DIR = os.getcwd()
    
    return BASE_DIR


def create_dir(dir_name: str) -> str:
    BASE_DIR = get_corrent_path()
    dir_path = os.path.join(BASE_DIR, dir_name)
    if  not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    return dir_path


def create_file(file_name: str, dir_path: str) -> str:
    file_path = os.path.join(dir_path, file_name)
    if not os.path.isfile(file_path):
        with open(file_path, "w") as f:
            f.write("")
    return file_path


def check_contents(path: str):
    if not os.path.isdir(path):
        print(f"{path} not founded")
        return None
    names = os.listdir(path=path)
    for name in names:
        full_path = os.path.join(path, name)
        if os.path.isdir(full_path):
            print(f"DIR: {name}")
        elif os.path.isfile(full_path):
            print(f"FILE: {name}")
        else:
            print(f"OTHER: {name}")


if __name__ == "__main__":
    dir_name = "project_test"
    file_read = "readme.txt"
    file_data = "data.txt"
    
    dir_path = create_dir(dir_name)
    create_file(file_read, dir_path)
    create_file(file_data, dir_path)
    check_contents(dir_path)