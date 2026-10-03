university_portal_select = int(input('Are You A 1.Student Or 2.Teacher: '))

match university_portal_select:
    case 1:
        student_select = int(input('What do you want to select:\n1.View Courses\n2.View Marks\n3.View Attendance\n:'))
        match student_select:
            case 1:
                print('Opening Courses')
            case 2:
                print('Opening Marks')
            case 3:
                print('Opening Attendance')
    case 2:
        teacher_select = int(input('Where Do You Want To Go:\n1.View Students\n2.Enter Makrs\n3.View Attendance\n:'))
        match teacher_select:
            case 1:
                print('Opening Students Data')
            case 2:
                print('Opening Student Marks')
            case 3:
                print('Opening Attendance Portal')