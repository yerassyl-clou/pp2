def gen(n):
    num = 0
    while(num < n):
        yield num**2
        num += 1
    
x = int(input())

for i in gen(x):
    print(i, end=" ")