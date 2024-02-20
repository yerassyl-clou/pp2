#File handling


#Open file

f = open("vscode/kbtu/pp2/lecs/week6/row.txt", "r", encoding="UTF-8")


#Check in file

for x in f:
    if 'БИН' in x:
        print("Yes")
        print(x.split()[1].strip())                     # Вернуть все в строке после БИН

    



#Prices    

f = open("vscode/kbtu/pp2/lecs/week6/row.txt", "r", encoding="UTF-8")
flag = False

for x in f:
    if flag:
        print(x)
        flag = False
    if 'Стоимость' in x:
        flag = True