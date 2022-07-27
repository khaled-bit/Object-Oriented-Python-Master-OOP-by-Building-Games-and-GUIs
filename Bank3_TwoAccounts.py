account1Name=''
account1Balance=0
account1Pass=''

account2Name=''
account2Balance=0
account2Pass=''
nacc=0
def newAccount(accountNumber,name , balance,password):
    global account1Name,account1Balance,account1Pass
    global account2Name,account2Balance,account2Pass

    if accountNumber==0:
        account1Pass=password
        account1Name=account1Name
        account1Balance=balance

    if accountNumber==1:
        account2Pass=password
        account2Name=account1Name
        account2Balance=balance
    

def show():
     global account1Name,account1Balance,account1Pass
     global account2Name,account2Balance,account2Pass

     if account1Name!='':
        print('Account 1')
        print('     Name:',account1Name)
        print('     password:',account1Pass)
        print('     Balance',account1Balance)
     
     if account2Name!='':
        print('Account 2')
        print('     Name:',account2Name)
        print('     password:',account2Pass)
        print('     Balance',account2Balance)


def getBalance(accountnumber,password):
     global account1Name,account1Balance,account1Pass
     global account2Name,account2Balance,account2Pass

     if accountnumber==0:
        if password!=account1Pass:
            print('InCorrect pass')
            return None
        return account1Balance

     if accountnumber==1:
        if password!=account2Pass:
            print('InCorrect pass')
            return None
        return account2Balance
     
        



