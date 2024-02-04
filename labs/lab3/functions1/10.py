def myset(list):                                                        
    final = []

    for i in range(len(list)):                                  
        unique = True
        for j in range(i + 1, len(list)):           #starting from i+1 (before all elements are unique)
            if list[i] == list[j]:                  #if element repeating we skipping it
                unique = False
        if unique:
            final.append(list[i])                   #if elemen unique we adding it to final list
    
    return final



print(myset([1, 2, 3, 5, 11, 4, 4, 5, 6, 7, 8, 8, 8, 9, 10]))