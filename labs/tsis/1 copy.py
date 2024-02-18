def func(list):
    max = list[0]
    min = list[0]

    for x in range(len(list) - 1):
        if len(list[x]) > len(max):
            max = list[x]
        
        if len(list(len(list) - 1)) > len(list(len(list) - 2)):
            max = list(len(list) - 1)

    for i in range(len(list) - 1):
        if len(list[i]) < len(min):
            min = list[i]
        
        if len(list(len(list) - 1)) < len(list(len(list) - 2)):
            min = list(len(list) - 1)
        

    return (min, max)

lst = ["1234", "123", "12345", "12"]

print(func(lst))