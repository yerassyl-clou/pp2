def trueFunc(t):
    if all(t): return True
    return False


tup = ("srt","245",335, "sdf")
print(trueFunc(tup))

tup = ("srt","245",335, "")
print(trueFunc(tup))
