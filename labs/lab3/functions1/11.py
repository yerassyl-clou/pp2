def palindrome(word):
    for i in range(round(len(word) / 2) + 1):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True

print(palindrome("madam"))