'''Problem statement:- Create a Python folder organizer application. This application is very useful when you need to organize a folder which has a lot of files.
We are going to use the OS module to make folders and sort the file based on their file extensions and move them into their respective folders.'''

import os, shutil
path = input("enter path: ")
files = os.listdir(path)
fileExtensions = set()
dirDict = {}

for item in files:
    itemParsed = item.split('.')
    fileExtensions.add(itemParsed[1])

for extension in fileExtensions:
    fileNames = set()
    for item in files:
        itemParsed = item.split('.')
        if itemParsed[1] == extension:
            fileNames.add(itemParsed[0])
        dirDict[extension] = fileNames

for key, values in dirDict.items():
    os.mkdir(f"{path}\.{key}")
    for item in values:
        shutil.move(f"{path}\{item}.{key}", f"{path}\.{key}")


