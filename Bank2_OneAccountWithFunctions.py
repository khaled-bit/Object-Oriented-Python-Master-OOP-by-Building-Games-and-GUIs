from re import A



accountName=''

accountPass=''

accountBalance=0

def newAccount(name,balance,password):
    accountName=name
    accountPass=password
    accountBalance=balance

def getBalance(password):
    if password ==accountPass:
        return accountBalance
    else:
        return None

def deposit(amounToDeposit, password):
    global accountName,accountBalance,accountPass
    
    if amounToDeposit < 0:
        print('you cannot deposit neg number')
    else:
        if accountPass==password:

           accountBalance = accountBalance + amounToDeposit
           return accountBalance
        else:
            return None

def withdraw(amounttoWithdraw , password):
        global accountName,accountBalance,accountPass
        if amounttoWithdraw < 0:
            print('You cannot withdraw a negative amount')
            return None
        if password != accountPass:
            print('Incorrect password for this account')
            return None
        if amounttoWithdraw > accountBalance:
            print('You cannot withdraw more than you have in your account')
            return None
        accountBalance = accountBalance - amounttoWithdraw
        return accountBalance

            
newAccount('khalid',1000,'khalid2000')


                   


            
while True:

   print()
   print('Press b to get the balance')
   print('Press d to make a deposit')
   print('Press w to make a withdrawal')
   print('Press s to show the account')
   print('Press q to quit')
   print()
   action = input('What do you want to do? ')
   action = action.lower() # force lowercase
   action = action[0] # just use first letter
   print()
   if action == 'b':
    print('Get Balance:')
    userPassword = input('Please enter the password: ')
    theBalance = getBalance(userPassword)
    if theBalance is not None:
     print('Your balance is:', theBalance)
   elif action == 'd':
     print('Deposit:')
     userDepositAmount = input('Please enter amount to deposit: ')
     userDepositAmount = int(userDepositAmount)
     userPassword = input('Please enter the password: ')
     newBalance = deposit(userDepositAmount, userPassword)
     if newBalance is not None:
        print('Your new balance is:', newBalance)