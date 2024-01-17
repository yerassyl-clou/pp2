txt = "KBTU is the best university"

print("best" in txt)            #"best" in txt - bool

x = "best" in txt

if x:
    print("best is in txt")

y = "worst"

if y not in txt:
    print("worst is NOT present")