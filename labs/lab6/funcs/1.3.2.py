a = [1,2,3,4,5]

lst = [a[:1]]

for x in a[1:]:

    for y in range(x):
        lst.append(x)
    
print(lst)