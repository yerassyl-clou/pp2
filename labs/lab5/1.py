import re 

txt = input()

pattern = "ab*"

res = re.search(pattern, txt)

print(res.string)
