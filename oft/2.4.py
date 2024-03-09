import time

def symbCoolPrint(char, null):
    asc = ord(char)
    cnt = 65

    empty = ""

    while True:
        empty += chr(cnt)
        time.sleep(0.01)
        print(null + chr(cnt))
        cnt += 1

        if cnt == 91:
            cnt = 97
        
        if cnt == asc+1 or cnt > 122:
            break

string = input("Str: ")

empt = ""

for x in string:
    print(empt, end="")
    print()
    symbCoolPrint(x, empt)
    empt += x