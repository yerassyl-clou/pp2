import os

path = input("path: ")

if os.access(path, os.F_OK):
    print("Path exists")
else:
    print("Path doesn't exists")

