# Q24. Online Exam Portal
# Create a menu:

# 1 → Start Exam
# 2 → View Result
# 3 → Exit
# If the user selects Start Exam, ask for age.

choice = int(input('----Menu----\n1.Start Exam\n2.View Result\n3.Exit'))

match choice:
    case 1:
        age = int(input('Enter Your Age: '))
        if age >=18:
            print('You Can Start The Exam')
        else:
            print('You Cannot Start The Exam')
    case 2:
        print('The Result Is A+')
    case 3:
        print('Exiting')
        