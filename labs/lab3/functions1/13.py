import random
guesNum = random.randrange(1, 21)


name = input("Hello! What is your name?\n")

txt1 = "\nWell, {}, I am thinking of a number between 1 and 20."
print(txt1.format(name))


number = int(input("Take a guess.\n"))


rightGuess = False
guessCounter = 1

txt2 = "\nGood job, {}! You guessed my number in {} guesses!"


while(not rightGuess):
    if number == guesNum:
        print(txt2.format(name, guessCounter))
        rightGuess = True

    elif number > guesNum:
        print("\nYour guess is too big.")
        number = int(input("Take a guess.\n"))
        guessCounter += 1

    else:
        print("\nYour guess is too low.")
        number = int(input("Take a guess.\n"))
        guessCounter += 1
    