accountList = []

def newAccount(aName,aBalance,aPass):
    dict={'name':aName , 'balance':aBalance,'password':aPass}
    accountList.append(dict)


def show(accountNumber):
    global accountList
    print('Account',accountNumber)
    thisAccountdict= accountList[accountNumber]
    print(' Name', thisAccountdict['name'])
    print(' Balance:', thisAccountdict['balance'])
    print(' Password:', thisAccountdict['password'])
    print()

def getBalance(accountNumber,password):
    global accountList
    thisAccountdict= accountList[accountNumber]

    if password!=thisAccountdict['password']:
        print('Incorrect password')
        return None
    return thisAccountdict['balance']

    
    