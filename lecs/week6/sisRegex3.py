import re                                                                                   #git 14.py

f = open("vscode/kbtu/pp2/lecs/week6/row.txt", "r", encoding="UTF-8")

text = f.read()


KKMpattern = r"\n.+(РНМ).*(?P<KKMpattern>[0-9]{12})"                
BINpattern = r"\nБИН\s+(?P<BIN>[0-9]{12})"                 #([0-9]{12}) - group named "BIN"

KKMvalue = re.search(KKMpattern, text)
BINvalue = re.search(BINpattern, text).group('BIN')



if KKMvalue:
    print(KKMvalue.group('KKMpattern'))
else:
    print("not found")

if BINvalue:
    print(BINvalue.group('KKMpattern'))
else:
    print("not found")