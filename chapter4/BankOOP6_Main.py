
from bankoop6_modified import *

oBank = Bank('9 to 5','123 Main Street , Anytown ,USA','01111324055')

while True:
    print()
    print('to get an account balance press b')
    print('to close account, press c')
    print('to make a deposit press d')
    print('to get bank information press i ')
    print('to open a new account press o')
    print('to quit press q')
    print('to show all accounts press s')
    print('to make a withdrawal press w')
    print()

    action = input('What do you want to do ?')
    action = action.lower()
    action = action[0]
    print()

    try:
        if action=='b':
            oBank.getBalance()
        elif action=='c':
            oBank.closeAccount()
        elif action=='i':
            oBank.getInfo()
        elif action=='o':
            oBank.openAccount()
        elif action=='q':
            break

        elif action=='s':
            oBank.show()
        elif action =='w':
            oBank.withdaw()

    except AbortTransaction as error:
        print(error)
    

