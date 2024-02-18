import datetime

def dates(year, month, day):
    input_date = datetime.date(year, month, day)
    
    yesterday = input_date - datetime.timedelta(days=1)
    tomorrow = input_date + datetime.timedelta(days=1)
    
    print("Yesterday:", yesterday)
    print("Today:", input_date)
    print("Tomorrow:", tomorrow)

year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

dates(year, month, day)
