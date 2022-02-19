import os

path, folders, files = next(os.walk(r"C:\Users\Avinash\Desktop\flask_application"))
file_count = len(files)
folders_count=len(folders)
print(f"number of files in directory : {file_count} and available files are : {files}")
print(f"number of folders in directory : {folders_count} and available folders are : {folders}")