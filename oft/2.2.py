import time

str = "Hello world!"

empty = ""

for x in str:
    asc = ord(x)
    cnt = 0

    while cnt != asc:
        cnt += 1
    
    empty += chr(cnt)

    time.sleep(0.1)
    print(empty)

