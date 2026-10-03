user_food=int(input('Enter The Food Number You Want To Order\n1.Pizza\n2.Burger\n3.Pasta\n4.Sandwich\nEnter Your Choice:=>'))

match user_food:
    case 1:
        print('You Selected Pizza')
    case 2:
        print('You Selected Burger')
    case 3:
        print('You Selected Pasta')
    case 4:
        print('You Selected Sandwich')
    case default:
        print('Invalid Menu Choice')
        
        