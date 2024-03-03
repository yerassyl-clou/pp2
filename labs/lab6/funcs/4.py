import time 

def sqrt(x):
    return x**0.5

def delPrint(x, delTime):
    time.sleep(delTime/1000)
    return sqrt(x)

num = int(input())
delTime = int(input())

txt = "Square root of {} after {} miliseconds is {}"

print(txt.format(num, delTime, delPrint(num, delTime)))
