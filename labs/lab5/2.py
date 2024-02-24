import re 

txt = input()

pattern = "ab{2}|b{3}"

res = re.search(pattern, txt)

if res:
    print(res.string)
else:
    print("No match")