from Account import *

accountList = []

print('Nour account numebr is 0')
oAccount = Account('nourseen',100,'nour')
accountList.append(oAccount)
print('enas account number is 1')
oAccount = Account('Enas',100,'enas')
accountList.append(accountList)
print('ramez account number is 2')
oAccount = Account('ramez',100,'ramez')
accountList.append(oAccount)

accountList[0].show()
accountList[1].show()
accountList[2].show()

print('calling methods')

accountList[0].deposit(50,'nour')
accountList[1].deposit(50,'enas')
accountList[2].deposit(50,'ramez')


accountList[0].show()
accountList[1].show()
accountList[2].show()

#creating account from inpurt from user

userName = input('enter ur name : ')
userPass = input('enter ur pass : ')
userBalance = input('enter ur balance: ')
print('account number is 3')
oAccount = Account(userName,userBalance,userPass)
accountList.append(oAccount)

accountList[3].show()

#problem we face when use list
#we have 5 acc and acc no 2 want to clsoe acc

accountLists = []
oAccount = Account('nourseen',100,'nour')
accountLists.append(oAccount)
oAccount = Account('Enas',200,'enas')
accountLists.append(oAccount)
oAccount = Account('ramez',4400,'ramez')
accountLists.append(oAccount)
oAccount = Account('hosni',112300,'hosni')
accountLists.append(oAccount)
oAccount = Account('khaled',1030,'khaled')
accountLists.append(oAccount)
accountLists[0].show()
accountLists[1].show()
accountLists[2].show()
accountLists[3].show()
accountLists[4].show()
accountLists.pop(2)
accountLists[0].show()
accountLists[1].show()
accountLists[2].show()
accountLists[3].show()
accountLists[4].show()
