a = (1,2,3,4,5)

lst = (a[:1])

for x in a[1:]:
    lst *= x
    
#print(lst)
print(sum(lst))