from Account import *

accountDict = {}
nextAccountNumber = 0

oAcc = Account('khaled',100,'khaled')
accountDict[nextAccountNumber] = oAcc
nextAccountNumber = nextAccountNumber + 1
oAcc = Account('ahmed',100,'ahmed')
accountDict[nextAccountNumber] = oAcc
nextAccountNumber = nextAccountNumber + 1
oAcc = Account('lila',100,'lila')
accountDict[nextAccountNumber] = oAcc