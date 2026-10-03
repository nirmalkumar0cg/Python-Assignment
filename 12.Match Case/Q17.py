atm_withdraw = int(input('Account Type?\n1.Savings\n2.Current\n: '))

match atm_withdraw:
    case 1:
        print('Savings Account')
        saving_option=int(input('What Do You Want To Do\n1.Check Balance Of Savings\n2.Deposit Savings\n3.Withdraw Savings\n:'))
        match saving_option:
            case 1:
                print('Check Balance Selected')
            case 2:
                print('Depost Savings Selected')
            case 3:
                print('Withdraw Savings Selected')
    case 2:
        print('Current Account')
        current_option=int(input('What Do You Want To Do\n1.Check Balance Of Current\n2.Deposit\n3.Withdraw\n:'))
        match current_option:
            case 1:
                print('Check Balance Selected')
            case 2:
                print('Depost Selected')
            case 3:
                print('Withdraw Savings Selected')