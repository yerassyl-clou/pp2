def isPrime(a):

    if a < 2:
        return False
    
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True



lst = list(range(100))

primes = list(filter(lambda x: isPrime(x), lst))

print(primes)