import re                                                                              

f = open("vscode/kbtu/pp2/lecs/week6/row.txt", "r", encoding="UTF-8")

text = f.read()


pattern = r"\n(?P<order>[0-9]+)\."

res = re.search(pattern, text)



print(res.group('order'))