from Account import *

oKhaledAccount = Account('khaled',100,'khpass')
print('Created Account for khaled')

oAmirAccount = Account('amir',100,'Amirpass')
print('account created fror amir')

oKhaledAccount.show()
oAmirAccount.show()

print('calling some methods of 2 accounts')

oKhaledAccount.deposit(50,'khpass')
oKhaledAccount.deposit(50,'khpass3')
oAmirAccount.deposit(11,'2')
oAmirAccount.deposit(11,'AmirPass')
oKhaledAccount.deposit(10,'khpass')
oKhaledAccount.show()
oKhaledAccount.withdraw(10,'khpass')
oKhaledAccount.show()

#Creating 3rd Acc
userName = input('please enter ur name')
userPass = input('please enter ur pass')
userBalance = input('please enter ur balance')

oMaiAccount = Account(userName,userBalance,userPass)

oMaiAccount.show()