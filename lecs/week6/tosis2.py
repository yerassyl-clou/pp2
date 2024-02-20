f = open("vscode/kbtu/pp2/lecs/week6/row.txt", "r", encoding="UTF-8")



flag = False

for x in f:
    if flag:
        print(x)
        flag = False
    if 'Стоимость' in x:
        flag = True