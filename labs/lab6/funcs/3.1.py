def isPal(string):
    str = reversed(string)
    rev = ""

    for x in str:
        rev += x

    if rev == string:
        return True
    return False

print(isPal("abcba"))
print(isPal("abcbda"))