
#CUSTOM EXCEPTION

class AbortTransaction(Exception):
    '''abort bank transaction'''
    #print("aaaaaa")
    pass


class Account():

    def __init__(self,name,balance,password):
        self.name=name
        self.balance=balance
        self.password=password

    def validateAmount(self,amount):

        try:
            amount = int(amount)

        except ValueError:
            print('sorry')

            raise AbortTransaction('Amount Must be Integer')
        if amount <=0:
            raise  AbortTransaction('Amount must be positive')
            #print('sorry1')
        #print('333')
        return  amount

    def checkPassworMatch(self,password):
        if password!=self.password:
            raise AbortTransaction('Incorrect Password for this Account')

    def deposit(self,amountToDeposit):
        amountToDeposit = self.validateAmount(amountToDeposit)
        self.balance = self.balance + amountToDeposit
        return self.balance

    def getBalance(self):
        return self.balance


    def withdraw(self,amounToWithdraw):
        amounToWithdraw = self.validateAmount(amounToWithdraw)
        if amounToWithdraw > self.balance:
            raise AbortTransaction('must be entering less number')

        self.balance = self.balance - amounToWithdraw
        return self.balance


    def show(self):

        print(' Name:', self.name)
        print(' Balance:', self.balance)
        print(' Password:', self.password)


oac1= Account('khaled',5,'123')
oac1.withdraw(-4)