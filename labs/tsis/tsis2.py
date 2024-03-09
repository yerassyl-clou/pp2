#day second month

import datetime

def Dif(date1, date2):
    
    dif = date1 - date2

    return dif.total_seconds()




now = datetime.datetime.now()

birth = datetime.datetime(2006, 4, 24)

seconds = Dif(now, birth)

print("Seconds: " + str(Dif(now, birth)))


print("Days:" + str(seconds/(60*24*60)))


print("Minutes: " + str(seconds/60))