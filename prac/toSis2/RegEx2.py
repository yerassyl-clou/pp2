import re

f = open("prac/toSis2/RegEx.txt", "r", encoding="UTF-8")

txt = f.read()

"""
for x in f:
    print(x, end="")
"""

pattern = r""

res = re.search(pattern, txt)

if res:
    print(res.string)
else:
    print("404")