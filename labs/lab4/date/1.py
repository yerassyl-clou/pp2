import datetime

def subtr5dates():
    date = datetime.datetime.now()
    day = int(date.strftime("%j"))
    year = int(date.strftime("%Y"))

    if day > 5:
        return day - 5
    else:
        if year % 4 == 0:
            return 366 + day - 5
        else:
            return 365 + day - 5 

print(subtr5dates())