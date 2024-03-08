import datetime

y = 2024
m = 7
d = 13

daydiff = 24

date = datetime.datetime(y, m, d)
date2 = datetime.timedelta(days=daydiff)

date3 = date - date2

print(date3)
