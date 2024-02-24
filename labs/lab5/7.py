import re           #snake -> camel

txt = input()

res = re.sub(r"_(\w)", lambda x: x[1].upper(), txt)

if res:
    print(res)
else:
    print("No match")