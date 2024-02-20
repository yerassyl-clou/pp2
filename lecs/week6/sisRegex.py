import re

f = open("vscode/kbtu/pp2/lecs/week6/row.txt", "r", encoding="UTF-8")

text = f.read()


BINpattern = r"\nБИН\s+(?P<BIN>[0-9]{12})"                 #([0-9]{12}) - group named "BIN"

print(re.search(BINpattern, text).group('BIN'))             #Обращение к группе 'BIN' по патерну BINpattern