# Q23. ATM Withdrawal
# Create an ATM withdrawal program.

# First use match-case for:

# 1 → Savings
# 2 → Current
# For either account, ask for withdrawal amount.

choice = int(input('Which Account?\n1.Saving\n2.Current\n: '))

match choice:
    case 1:
        amt = int(input('Enter The Amount You Want To Withdraw: '))
        if amt < 0:
            print('Invalid Amount')
        else:
            print('Wthdrawal Request Accepted')
    case 2:
        amt = int(input('Enter The Amount You Want To Withdraw: '))
        if amt < 0:
            print('Invalid Amount')
        else:
            print('Wthdrawal Request Accepted')
        
        