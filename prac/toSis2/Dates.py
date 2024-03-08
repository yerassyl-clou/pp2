import datetime

x = datetime.datetime.now()

print(x.year, end = "-")
print(x.month, end = "-")
print(x.day, end = "-")
print(x.hour, end = "-")
print(x.minute, end = "-")
print(x.second, end = "-")
print(x.microsecond % 100)

"""

%a      Wed Thu Mon
%A      Wednesday Monday
%w      0 (Monday) 6 (Sunday)
%d      0-31 (Month day)
%b      Dec Jan Feb
%B      December
%m      01 (Jan) 02 (Fab)
%y      0-99 (short year)
&Y      2024 
%H      00-23 (Hour)
%I      00-12 (Hour)
%p      AM/PM
%M      00-59 (Min) 
%S      00-59 (Sec)
%f      000000-999999 (Microsec)
%z      UTC    
%j      001-366 (day num of yaer)

print(x.strftime(%))

"""