import re

f = open("lecs/week6/row.txt", "r", encoding="UTF-8")

text = f.read()


KKMpattern = r"\n.+(РНМ).*(?P<KKMpattern>[0-9]{12})"                

result = re.search(KKMpattern, text)

if result:
    print(result.group('KKMpattern'))
else:
    print("not found")