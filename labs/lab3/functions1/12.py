def histogram(list):
    for i in range(len(list)):

        str = ""

        for j in range(list[i]):
            str += "*"
            
        print(str)

histogram([4, 9, 7])