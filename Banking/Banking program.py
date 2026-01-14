

def is_balance():
    print("*****************************")
    print(f"Your Balance is ${balance:.2f}")
    print("*****************************")

def deposit():
    amount = float(input("Enter the amount that you want to deposit:"))

    if amount<=0:
        print("*****************************")
        print("Enter a valid amount")
        print("*****************************")
        return 0
    else:
        return amount
        
def withdraw():
    amount= float(input("Enter the amount that you want to withdraw:"))

    if amount <= 0:
        print("*****************************")
        print("Enter a valid amount to withdraw")
        print("*****************************")
        return 0
    elif amount> balance:
        print("*****************************")
        print("Not enough balance")
        print("*****************************")
        return 0
    else:
        return amount



balance = 0
run=True


while run:
    print("*****************************")
    print("      Banking Program        ")
    print("*****************************")
    print("Enter 1 to Check the balance")
    print("Enter 2 to withdraw amount")
    print("Enter 3 to deposit amount")
    print("Enter 4 to Exit")
    print("*****************************")
    print( )

    case = int(input("Enter your selection (1-4): "))

    if case == 1:
        is_balance()
    elif case == 2:
        withdraw_amount = withdraw()
        if withdraw_amount > 0:
            balance -= withdraw_amount
            print("*****************************")
            print(f"${withdraw_amount:.2f} withdrawn successfully")
            print(f"Your current balance is ${balance:.2f}")
            print("*****************************")
        else:
            print("*****************************")
            print(f"Your current balance is ${balance:.2f}")
            print("*****************************")

    elif case == 3:
        deposit_amount= deposit()
        if deposit_amount>0:
            balance += deposit_amount
            print("*****************************")
            print(f"${deposit_amount:.2f} deposited successfully")
            print(f"Your current balance is ${balance:.2f}")
            print("*****************************")
        else:
            print("*****************************")
            print(f"Your current balance is ${balance:.2f}")
            print("*****************************")
    elif case == 4:
        print("Thank you for using Banking program, Have a nice day")
        run= False
    else:
        print("*****************************")
        print("     Invalid Response        ")
        print("*****************************")