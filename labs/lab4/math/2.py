def trapArea(height, base1,base2):
    return height * ((base1 + base2) / 2)

x = int(input("Height: "))
y = int(input("Base, first value: "))
z = int(input("Base, second value: "))

txt = "Expected Output: {}"
print(txt.format(trapArea(x, y, z)))