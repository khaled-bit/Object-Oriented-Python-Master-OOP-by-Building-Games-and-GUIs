from argparse import Action


accountName = 'Khalid'
accountPassword='khalid2000'
accountBalance = 500


while True:
    print()
    print('press b to get balance')
    print('press d to get deposit')
    print('press w to make a withdraw')
    print('press s to show info')
    print('press q to quit')
    print()

    action = input(' What you want to do ?')
    action = action.casefold()

    if action=='b':
        print('Get balacne now')
        usPass= input('please enter ur password')
        if usPass==accountPassword:
            print('your balance is' + str(accountBalance))
        else:
            print('InCorrect Password')
    

    if action=='d':
        print('Please enter amount to deposit and pass')
        userDepositAmount = input('please enter amount to deposit')
        usPass= input('please enter ur password')
        userDepositAmount = int(userDepositAmount)
        if usPass==accountPassword:
            if userDepositAmount < 0:
                print('You can not deposit a neg number')
  
             
            else:
                accountBalance = accountBalance + userDepositAmount
                print('Your new balance is:', accountBalance)
        else:
            print('InCorrect Password')


    if action=='s':
        print('show:')
        print('     Name',accountName)
        print('     Balance',accountBalance)
        print('     password',accountPassword)        
        print()

    elif action =='q':
        break

    elif action=='w':
        print('Withdraw:')
        userWithdrawAmount = input('enter the amount you want to withdraw  and pass')
        userWithdrawAmount = int(userWithdrawAmount)
        usPass= input('please enter ur password')
        if userWithdrawAmount < 0:
            print('You cannot withdraw a negative amount')
        elif usPass != accountPassword:
            print('Incorrect password for this account')
        elif userWithdrawAmount > accountBalance:
            print('You cannot withdraw more than you have in your account')
        else:
            accountBalance = accountBalance - userWithdrawAmount
            print('Your new balance is:', accountBalance)



        