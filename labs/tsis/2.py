word = "w1r3f4"

result = ""
for i in range(len(word)):
    if word[i] == "0" or word[i] == "1" or word[i] == "2" or word[i] == "3" or word[i] == "4" or word[i] == "5" or word[i] == "6" or word[i] == "7" or word[i] == "8" or word[i] == "9":
        result += str(i)

print(result)