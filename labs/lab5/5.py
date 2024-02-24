import re 

txt = input()

pattern = "a.*b$"
res = re.search(pattern, txt)

if res:
    print(res.string)
else:
    print("No match")