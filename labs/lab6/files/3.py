import os

path = input("Enter path: ")

if os.access(path, os.F_OK):
    print("path: " + path)
    print("basename: " + os.path.basename(path))
    print("dirname: " + os.path.dirname(path))
else:
    print("Path doesn't exists")

