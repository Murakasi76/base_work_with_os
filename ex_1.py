#!/usr/bin/env python3
import os

def work_with_dir(path_for_new_dir: str):
    try:
        files = os.listdir(path_for_new_dir)
    except FileNotFoundError:
        print("not found dir")
        return None
    with open(os.path.join(path_for_new_dir, "file_info.txt"), "w") as f:
        f.write(f"=== Files from {path_for_new_dir}===\n")
        if not files:
            f.write("No files")
        for file in files:
            if os.path.isfile(os.path.join(path_for_new_dir, file)):
                f.write(file + "\n")
    


    
if __name__ == "__main__":
    if os.name == "posix":
        work_with_dir("/tmp")
        print("Done")
    else:
        work_with_dir("C:\\Download")
        print("Done")