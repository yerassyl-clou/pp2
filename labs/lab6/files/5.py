f = open("labs/lab6/files/5.txt", "w")

lst = [123, 456, "abcde", "qwerty", True]

for x in lst:
    f.write(str(x))
    f.write(", ")