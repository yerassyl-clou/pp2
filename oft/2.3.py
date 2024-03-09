import time

def symbCoolPrint(char, null):
    asc = ord(char)
    cnt = 65

    empty = ""

    while cnt != asc and cnt <= 122:
        empty += chr(cnt)
        time.sleep(0.01)
        print(null + chr(cnt))
        cnt += 1

        if cnt == 91:
            cnt = 97

string = input("String: ")

empt = ""

for x in string:
    print(empt, end="")
    symbCoolPrint(x, empt)
    empt += x

print(empt)
