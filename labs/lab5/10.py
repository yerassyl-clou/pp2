import re           #camel -> snake         camelCaseString

txt = input()

res = re.sub(r"[A-Z]",lambda x: "_" + x[0].lower(), txt)

if res:
    print(res)
else:
    print("No match")