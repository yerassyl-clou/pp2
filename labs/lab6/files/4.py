f = open("labs/lab6/files/4.txt")

data = f.readlines()                        #прочитать все линии

cnt = 0

for x in data:                              #пройти по каждой строке
    cnt += 1                                #посчитать каждую

print(cnt)