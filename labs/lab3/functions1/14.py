from functions import solve
from functions import isPrime
from functions import histogram

heads = int(input("Heads amount: "))
legs = int(input("Legs amount: "))

print(solve(heads, legs))



histogram(solve(heads, legs))




a, b = solve(heads, legs)

if isPrime(a):
    print("Amount of chickens is prime")
else:
    print("Amount of chickens is not prime")


if isPrime(b):
    print("Amount of rabbits is prime")
else:
    print("Amount of rabbits is not prime")
