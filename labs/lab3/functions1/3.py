heads = 35
legs = 94

def solve(heads, legs):
    for i in range(heads):
        chikens = i
        rabbits = heads - i

        chikensLegs = chikens * 2
        rabbitsLegs = rabbits * 4

        if chikensLegs + rabbitsLegs == legs:
            return (chikens, rabbits)
        
print(solve(heads, legs))
