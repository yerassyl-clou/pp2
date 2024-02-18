def solve(heads, legs):
    for i in range(heads):
        chikens = i
        rabbits = heads - i

        chikensLegs = chikens * 2
        rabbitsLegs = rabbits * 4

        if chikensLegs + rabbitsLegs == legs:
            return (chikens, rabbits)
        

def isPrime(a):

    if a < 2:
        return False
    
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True


def histogram(list):
    for i in range(len(list)):

        str = ""

        for j in range(list[i]):
            str += "*"
            
        print(str)