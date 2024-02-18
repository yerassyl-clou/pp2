def gen(n):
    num = 0
    while(num < n):
        if (num % 2 == 0):
            yield num
        num += 1
    
x = int(input())

for i in gen(x):
    print(i, end=",")