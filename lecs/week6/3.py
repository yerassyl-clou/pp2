#Regular expressions        (Automata)



#check email:

str = input("email:")               

parts = str.split('@')              #need to check for @

if len(parts) == 2:
    print(parts[0])
    print(parts[1])
else:
    print("no")



