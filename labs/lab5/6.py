import re 

txt = input()

res = re.sub("\s|[.]|[,]", ":", txt)

if res:
    print(res)
else:
    print("No match")