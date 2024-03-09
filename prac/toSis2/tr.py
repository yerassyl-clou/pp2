import datetime

y = int(input("y: "))
m = int(input("m: "))
d = int(input("d: "))

time = datetime.datetime(y,m,d)

delta = int(input("add to: "))

timeDelta = datetime.timedelta(days=delta)

smd = time + timeDelta

print(smd.strftime("%m"))
