def gen(a, b):
    num = a
    while(num < b):
        
        yield num**2
        num += 1
    
a = int(input())
b = int(input())

for i in gen(a, b):
    print(i, end=" ")