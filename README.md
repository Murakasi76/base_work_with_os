# Python OS Module Practice

This project contains exercises to practice working with the `os` module in Python, including handling directories, files, and file system checks. All three exercises are implemented in a single Python script.

---

## Exercises

### 1. List Files in a Directory
**Task:**  
- Write a function that takes a directory path and writes all filenames into a text file.  
- Only include files (skip directories).  
- If the directory is empty, write "No files".

**Purpose / Learning Outcome:**  
- Understand how to list directory contents using `os.listdir()`.  
- Learn to distinguish between files and directories using `os.path.isfile()`.  
- Practice writing output to a text file with Python.

---

### 2. Create a New Directory and a File
**Task:**  
- Create a function that creates a new folder in the current working directory.  
- Inside that folder, create a file named `hello.txt` and write `"Hello from Python"` in it.  
- Return the path to the created file.

**Purpose / Learning Outcome:**  
- Learn how to create directories using `os.mkdir()`.  
- Practice creating and writing files in Python.  
- Understand building file paths with `os.path.join()`.

---

### 3. Check File Existence and Readability
**Task:**  
- Write a function that takes a file path.  
- Check if the file exists and is readable.  
- If so, read and print its contents.

**Purpose / Learning Outcome:**  
- Learn how to check file existence and permissions using `os.access()`.  
- Understand file handling and reading content safely.  
- Combine knowledge of file paths and OS-level checks.

---

### Summary
By completing these exercises, you will gain practical experience with:  
- Navigating and manipulating the file system in Python.  
- Checking file and directory properties.  
- Combining `os` module functions to build simple file management scripts.

# File & Directory Manager in Python

## Overview
This project is a simple Python script that demonstrates how to work with **directories and files** using the built-in `os` module.  
It creates a new directory, generates text files inside it, and then lists all contents of the directory (distinguishing between files, folders, and other types).

---

## Features
- Detects the current working directory of the script.  
- Creates a new directory (`project_test`) if it does not exist.  
- Creates two files inside this directory:
  - `readme.txt`
  - `data.txt`
- Prints the directory contents:
  - `DIR: ...` → for subdirectories  
  - `FILE: ...` → for regular files  
  - `OTHER: ...` → for other types (symlinks, sockets, devices, etc.)

---

## Example Output
```bash
FILE: readme.txt
FILE: data.txt

