import re

with open("prac/toSis2/RegEx1.txt") as f:
    text = f.read()

pattern = r'\w*abab\w*'
results = re.findall(pattern, text)

if results:
    for result in results:
        print(result)
else:
    print("404")
