choice = int(input('----Main Menu----\n1.Emloyee\n2.Manager\n: '))

match choice:
    case 1:
        employee_choice = int(input('----Employee Options----\n1.View Profile\n2.Apply Leave\n3.View Salary\n: '))
        match employee_choice:
            case 1:
                print('Viewing Profile')
            case 2:
                days_off = int(input('Enter The Amount Of Leave You Want: '))
                if days_off == 0:
                    print('Invalid Leave Days')
                else:
                    print('Leave Request Submitted.')
    case 2:
        manager_choice = int(input('----Manager Options----\n1.View Team\n2.Approve Leave\n3.View Reports\n: '))
        match manager_choice:
            case 1:
                print('Viewing Team')
            case 2:
                print('Approving Leave of the employee')
            case 3:
                print('Viewing Reports')
