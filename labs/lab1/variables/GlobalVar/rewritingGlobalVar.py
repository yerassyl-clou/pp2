x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is", x)

myfunc()                            # fantastic     - local var

print("Python is", x)               # awesome       - global var
