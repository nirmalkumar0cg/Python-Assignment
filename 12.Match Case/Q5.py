user_input=input('Enter Choice: ')

match user_input:
    case 1:
        print('View Profile')
    case 2:
        print('View Courses')
    case 3:
        print('View Makrs')
    case 4:
        print('View Attendance')
    case 5:
        print('LogOut')
    case _:
        print('invalid choice')