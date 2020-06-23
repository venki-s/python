class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print('Account owner : {} ' .format(self.owner))
        print('Account balance : {} ' .format(self.balance))

    def deposit(self, amount):
        print('Deposit accepted')
        self.balance = self.balance + amount

    def withdraw(self, amount):

        if (self.balance < amount):
            print('Insufficient balance')
        else:
            self.balance = self.balance - amount


acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
print(acct1.balance)
acct1.withdraw(75)
print(acct1.balance)
acct1.withdraw(500)
print(acct1.balance)