class Account():
    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount
        return self.balance 
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return self.balance
        print("amount exceed!")
        return self.balance


prof = Account("Me", 120000)

prof.deposit(50000)
print(prof.balance)

prof.withdraw(15000)
print(prof.balance)

prof.withdraw(130000)
print(prof.balance)

prof.withdraw(30000)
print(prof.balance)

prof.deposit(25000)
print(prof.balance)
