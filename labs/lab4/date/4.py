import datetime

def secondsDif(year1, month1, day1, year2, month2, day2):
    date1 = datetime.datetime(year1, month1, day1)
    date2 = datetime.datetime(year2, month2, day2)

    dif = date1 - date2

    return dif.total_seconds()


y1 = int(input("Year 1: "))
m1 = int(input("Month 1: "))
d1 = int(input("Day 1: "))

y2 = int(input("Yeras 2: "))
m2 = int(input("Month 2: "))
d2 = int(input("Day 2: "))

print(secondsDif(y1, m1, d1, y2, m2, d2))