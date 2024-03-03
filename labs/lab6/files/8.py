import os

path = input("Enter path: ")  # For example: labs/lab6/files/8.txt

if os.access(path, os.F_OK | os.W_OK):
    os.remove(path)
    print("removed")
else:
    print("error")
