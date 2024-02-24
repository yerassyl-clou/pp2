import re 

txt = input()

pattern = "([a-z]_)+[a-z]"

res = re.search(pattern, txt)

if res:
    print(res.string)
else:
    print("No match")