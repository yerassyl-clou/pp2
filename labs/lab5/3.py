import re 

txt = input()

pattern = "\b[a-z]+_[a-z]+\b"

res = re.search(pattern, txt)

if res:
    print(res.string)
else:
    print("No match")