def f(n):
    a, b = 0, 1
    cnt = 2
    yield a

    while cnt < n:
        yield b

        c = a + b
        a = b
        b = c
        cnt += 1

n = int(input("n: "))

for i in f(n):
    print(i)