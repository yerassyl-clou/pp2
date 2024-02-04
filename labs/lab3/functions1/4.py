def isPrime(a):

    if a < 2:
        return False
    
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

def filter_prime(lst):  
    f = []
    for x in lst:
        if isPrime(x):
            f.append(x)
    return f

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(filter_prime(my_list))

