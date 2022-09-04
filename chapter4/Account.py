

class Account():
    def __init__(self , name , balance , password):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self , amountToDeposit ,passowrd):
        if passowrd!=self.password:
            print('sorry can not log in')
            return None
        if amountToDeposit <0:
            print('can not Deposit negative amount')
            return None

        self.balance = self.balance + amountToDeposit

        return self.balance

    def withdraw(self,amountToWithdraw,password):
        if password!=self.password:
            print('sorry can not log in')
            return None
        if amountToWithdraw>self.balance:
            print('sorry can not withdraw amount larger than balance')
            return None
        if amountToWithdraw <0:
            print('sorry can not withdraw amount less than zero')
        self.balance = self.balance - amountToWithdraw
        return self.balance

    def getBalance(self,password):
        if password!=self.password:
            print('sorry can not log in')
            return None
        return  self.balance



    def show(self):

        print(f'Name:{self.name:4}')
        print(f'Balance:{self.balance:4}')


#oAcc = Account('Khaled',1000,'khaled123')
#print(oAcc.deposit(500,'khaled123'))
#oAcc.deposit(500,'khaled122')