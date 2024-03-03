f = open("labs/lab6/files/4.txt")

data = f.readlines()

cnt = 0

for x in data:
    cnt += 1

print(cnt)