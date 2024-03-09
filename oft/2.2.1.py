import time

def symbCoolPrint(char):
    asc = ord(char)
    cnt = 65

    empty = ""

    while cnt != asc and cnt <= 122:
        empty += chr(cnt)
        time.sleep(0.01)
        print(chr(cnt))
        cnt += 1

        if cnt == 91:
            cnt = 97

    time.sleep(0.05)
    print(chr(cnt))

symbCoolPrint("s")