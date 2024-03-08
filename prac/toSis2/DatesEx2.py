import datetime

year = int(input(""))
month = int(input(""))
day = int(input(""))


x = datetime.datetime(year, month, day)

print(x.strftime("%A"))