user_input = input('Enter The Your Role: ')

match user_input:
    case 'admin':
        print('full access')
    case 'teacher':
        print('teacher dashboard')
    case 'student':
        print('student dashboard')
    case 'guest':
        print('limited access')
    case _:
        print('invalid role')