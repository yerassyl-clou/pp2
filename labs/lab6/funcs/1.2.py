lst = (5,2,3)                   #Не работает для n > 3

lst2 = lst[1:]
sum = sum(lst2) + 1

print(lst[0]*sum)