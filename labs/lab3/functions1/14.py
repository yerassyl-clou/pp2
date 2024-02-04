def solve(heads, legs):                                             # 35 , 94
    for i in range(heads):
        chikens = i
        rabbits = 35 - i

        chikensLegs = chikens * 2
        rabbitsLegs = rabbits * 4

        if chikensLegs + rabbitsLegs == legs:
            return (chikens, rabbits)
        
def histogram(list):
    for i in range(len(list)):

        str = ""

        for j in range(list[i]):
            str += "*"
            
        print(str)

def isPrime(a):

    if a < 2:
        return False
    
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

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
