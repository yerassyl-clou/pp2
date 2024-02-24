import re         

txt = input()


res = re.sub(r"[A-Z]",lambda x: " " + x[0], txt)

if res:
    print(res)
else:
    print("No match")