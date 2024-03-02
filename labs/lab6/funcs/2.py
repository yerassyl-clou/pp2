def upperCnt(s):
    cnt = 0
    for x in s:
        if x.isupper():
            cnt += 1
    return cnt

print(upperCnt("SomeStrinG"))