f = open("labs/lab6/files/8.txt", "w")

for x in range(1,1000):
    f.write(str(x))
    f.write("\n")