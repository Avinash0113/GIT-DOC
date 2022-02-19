# input = Location
#
# Files, folders should delete
import os
# import shutil
# shutil.rmtree(r"C:\Users\Avinash\Desktop\dummy\html files")
for root,directory,file in os.walk(r"C:\Users\Avinash\Desktop\dummy"):
    # print(directory)
    for element,variable in directory:
        os.remove(element)
