def isPal(str):
    rev = ""
    rev = rev.join(reversed(str))

    if rev == str:
        return True
    return False

print(isPal("abcba"))
print(isPal("abcbda"))