from Account import *


class Bank():

    def __init__(self):
        self.accountDict = {}
        self.accountNumber = 0


    def createAccount(self,name,amt,passw):

        oAccount = Account(name,amt,passw)
        AccNum = self.accountNumber

        self.accountDict[AccNum]=oAccount
        self.accountNumber = self.accountNumber + 1
        return AccNum

    def openAccount(self):

        name = input("please enter ur name")
        amt = input('please enter the start amount')
        amt = int(amt)
        password = input('please enter ur pass')

        account_number  = self.createAccount(name,amt,password)

    def closeAccount(self):

        accNum = input('please enter ur acc number')

        del self.accountDict[accNum]


    def balance(self):

        accNum = input('please enter account number')
        accNum = int(accNum)
        passw = input('please enter account password')
        oAccount = self.accountDict[accNum]
        theBalance = oAccount.getBalance(passw)


    def deposit(self):

        accNum = input('please enter account number')
        accNum = int(accNum)
        passw = input('please enter ur pass')
        oAccount = self.accountDict[accNum]
        amt = input('please enter the start amount')
        amt = int(amt)
        oAccount.deposit(amt,accNum)


    def show(self):
        for userAccNum in self.accountDict:
            oAccount = self.accountDict[userAccNum]
            print('  Account:',userAccNum)
            oAccount.show()


    def withdraw(self):
        accNum = input('please enter account number')
        accNum = int(accNum)
        passw = input('please enter account password')

        oAccount = self.accountDict[accNum]
        amt = input('please enter the start amount')
        amt = int(amt)
        balance = oAccount.withdraw(amt,passw)
