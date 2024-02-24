import re 

txt = input()

pattern = "^[A-Z]{1}[a-z]+$"                  #"[A-Z][a-z]+" все строки со значениями

res = re.search(pattern, txt)

if res:
    print(res.string)
else:
    print("No match")