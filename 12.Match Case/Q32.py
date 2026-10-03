# Q32. School Management System
# Create a school management system.

# First select:

# 1 → Student
# 2 → Teacher
# 3 → Parent
# Student options:

# 1 → Marks
# 2 → Attendance
# 3 → Homework
# Teacher options:

# 1 → Enter Marks
# 2 → Attendance
# 3 → Assign Homework
# Parent options:

# 1 → Child Marks
# 2 → Child Attendance
# 3 → Contact Teacher
# Use nested match-case.

choice = int(input('----School Management System----\n1.Student\n2.Teacher\n3.Parent\n: '))

match choice:
    case 1:
        option = int(input('----Student Options----\n1.Marks\n2.Attendance\n3.Homework\n: '))
        match option:
            case 1:
                print("Viewing Marks")
            case 2:
                print("Viewing Attendance")
            case 3:
                print("Viewing Homework")
    case 2:
        option = int(input('----Teacher Options----\n1.Enter Marks\n2.Attendance\n3.Assign Homework\n: '))
        match option:
            case 1:
                print("Entering Marks")
            case 2:
                print("Taking Attendance")
            case 3:
                print("Assigning Homework")
    case 3:
        option = int(input('----Parent Options----\n1.Child Marks\n2.Child Attendance\n3.Contact Teacher\n: '))
        match option:
            case 1:
                print("Viewing Child Marks")
            case 2:
                print("Viewing Child Attendance")
            case 3:
                print("Contacting Teacher")