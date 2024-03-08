lst = [1, 2, 3, 4, 5]

myit = iter(lst)

for i in range(len(lst)):
    print(next(myit))
