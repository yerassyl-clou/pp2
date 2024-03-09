import random

f = open("prac/toSis2/file2.txt", "a")

x = random.randrange(0, 99999)
st = str(x) 

f.write("\n" + st)