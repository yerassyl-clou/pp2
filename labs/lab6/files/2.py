import os

def pathCheck(path):
    if os.access(path, os.F_OK):
        print("Path exists")
    else:
        print("Path doesn't exists")

    if os.access(path, os.R_OK):
        print("Path is readable")
    else:
        print("Path is not readable")

    if os.access(path, os.W_OK):
        print("Path is writable")
    else:
        print("Path is not writable")

    if os.access(path, os.X_OK):
        print("Path is executable")
    else:
        print("Path is not executable")




path = input("path: ")      

pathCheck(path)