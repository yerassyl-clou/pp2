import re 

txt = input()

pattern = "ab*"

res = re.search(pattern, txt)

if res:
    print(res.string)
else:
    print("No match")