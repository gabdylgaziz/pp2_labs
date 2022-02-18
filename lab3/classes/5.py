class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.bank = {}
        
    def createacc(self):
        self.bank[self.owner] = int(self.balance)
        
    def deposit(self, money):
        self.bank[self.owner]+=money
        
    def withdraw(self, money):
        if self.bank[self.owner] - money > 0:
            self.bank[self.owner]-=money
        else:
            self.bank[self.owner] = -1    
    def dispacc(self):
        return self.bank
        
acc1 = Account('Gabdylgaziz', '180000')
acc1.createacc()
acc1.deposit(200000)
acc1.withdraw(100000)
print(acc1.dispacc())

acc2 = Account('Yelaman', '0')
acc2.createacc()
print(acc2.dispacc())

acc3 = Account('Miras', '200000')
acc3.createacc()
print(acc3.dispacc())

acc4 = Account('Zhanel', '150000')
acc4.createacc()
print(acc4.dispacc())

acc5 = Account('Karina', '170000')
acc5.createacc()
print(acc5.dispacc())

acc6 = Account('Nurikk', '190000')
acc6.createacc()
print(acc6.dispacc())

        