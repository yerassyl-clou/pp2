def gen(n):
    num = n
    while(num > 0):
        
        yield num
        num -= 1
    
n = int(input())

for i in gen(n):
    print(i, end=" ")