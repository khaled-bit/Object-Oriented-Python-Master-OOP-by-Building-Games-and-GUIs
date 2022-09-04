from Account import *
class AbortTransaction(Exception):
    '''abort bank transaction'''
    #print("aaaaaa")
    pass
class Bank():

    def __init__(self,hrs,address,phone):
        self.accountsDict = {
        }
        self.hrs=hrs
        self.address=address
        self.phone=phone
        self.nextAccountNumber = 0

    def askForVaildAccountNumber(self):
        accNum = input('please enter account number')

        try:
            accNum = int(accNum)

        except ValueError:
            raise AbortTransaction('the account number must be integer')

        if accNum not in self.accountDict.keys():
            raise AbortTransaction('There is no account ' + str(accNum))
        return  accNum

    def askForVaildPassword(self,acc):
        passw = input('please enter the password')
        try:
            acc.checkPasswordMatch(passw)
        except AbortTransaction:
            raise AbortTransaction('Incorrect password')
        return passw

    def getUsersAccount(self):
        accnum = self.askForVaildAccountNumber()
        oacc = self.accountDict[accnum]
        self.askForVaildPassword(oacc)
        return accnum,oacc

    def deposit(self):
        print('*** DEPOSIT ***')
        _,oAcc = self.getUsersAccount()
        depositamt = input('please enter the amount you want to deposit')
        totalBalance = oAcc.deposit(depositamt)
        print('totalBalance ',totalBalance)


    def withdaw(self):
        print('***Withdraw***')
        _,oAcc = self.getUsersAccount()
        withdrawamt = input('please withdraw amount')
        totalbalance = oAcc.withdraw(withdrawamt)
        print('total balance',totalbalance)

    def getBalance(self):
        print('*** Get Balance ***')
        _, oacc = self.getUsersAccount()
        print('your balance is',oacc.getBalance())

    def getInfo(self):
        print('Hours',self.hrs)
        print('Address', self.address)
        print('Phone', self.phone)
        print('We currently have ', len(self.accountsDict),' account(s) open.')


    def show(self):
        print('*** SHOW ***')
        for userAccNum,oacc in self.accountDict.items():
            #oacc = self.accountsDict[userAccNum]
            print('account:',userAccNum)
            oacc.show()

    def openAccount(self):
        print('*** OPEN ACCOUNT ***')
        accName = input('enter ur new account name')
        accBal = input('enter start balance')
        accPassw = input('please enter pass')

        oAcc = Account(name=accName,balance=accBal,password=accPassw)
        newAccNum = self.nextAccountNumber
        self.accountsDict[newAccNum] = oAcc
        self.nextAccountNumber +=1
        print('your new account is successfully created! ')



    def closeAccount(self):
        accNum ,oacc = self.getUsersAccount()
        self.accountsDict.pop(accNum)
        print('account closed')
