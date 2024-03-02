def listMult(a):
    cnt = 1
    for x in a:
        cnt *= x

    return cnt

a =[2,3,4,5,6,7]
print(listMult(a))