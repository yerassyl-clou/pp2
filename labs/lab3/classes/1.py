class mySting:
    def __init__(self):
        self.inputedString = ""

    def getString(self):
        self.inputedString = input("Enter your string: ")

    def printString(self):
        print(self.inputedString.upper())


string = mySting()

string.getString()
string.printString()