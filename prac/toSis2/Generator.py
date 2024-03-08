def inf_seq(s, e):
    num = s
    while num <= e:
        yield num
        num += 1
    

lst = []

"""for i in inf_seq(10,20):
    print(i, end=" ")"""



for i in inf_seq(0,10):
    lst.append(i**2)

print(lst)