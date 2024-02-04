def reverseWord(str):                   #We are ready -> ready are We
    result = ""
    
    allWords = str.split()

    for i in range(len(allWords) - 1):                          # range is -1 to avoid extra space 
        result += allWords[len(allWords) - i - 1]
        result += " "
    
    result += allWords[0]                                       # avoid extra space

    return result


print(reverseWord("We are ready"))