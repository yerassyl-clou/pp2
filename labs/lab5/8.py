import re         

txt = input()


res = re.findall("[A-Z][a-z0-9]*", txt)         #or "[A-Z][^A-Z]"

if res:
    print(res)
else:
    print("No match")