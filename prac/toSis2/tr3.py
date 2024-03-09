import re
import random

txt=""

for i in range (15):
    txt += str(random.randrange(0,999999))
    txt += " "

pat1 = r"[0-9]*5[0-9]*5[0-9]*"
pat2 = r"10[0-9]*"

res1 = re.findall(pat1, txt)
res2 = re.findall(pat2, txt)

if res1:
    print(res1)
else:
    print("No string with two 5's")

if res2:
    print(res2)
else:
    print("No string with 10 in the beggining")