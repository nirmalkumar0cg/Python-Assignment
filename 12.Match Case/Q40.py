# Q40. Complete Mini Application — College Portal
# Create a small college portal.

# Main menu:

# 1 → Student
# 2 → Teacher
# 3 → Administration
# Student
# 1 → Profile
# 2 → Marks
# 3 → Attendance
# 4 → Courses
# Teacher
# 1 → Students
# 2 → Enter Marks
# 3 → Attendance
# 4 → Courses
# Administration
# 1 → Fees
# 2 → Admissions
# 3 → Notices
# 4 → Departments
# Requirements:

# Use match-case for the main menu.
# Use nested match-case for the selected role.
# Use case _ for invalid choices.
# Keep the program easy to read.
# Do not use if-elif-else for fixed menu choices.
# Sample Input
# Enter role: 1
# Enter option: 2
# Sample Output
# Opening Student Marks

choice = int(input('----Your Role---\n1.Student\n2.Teacher\n3.Administration\n: '))

match choice :
    case 1:
        student_choice=int(input('---Student Menu---\n1.Profile\n2.Marks\n3.Attendance\n4.Courses\n: '))
        match student_choice:
            case 1:
                print('Opening Profile')
            case 2:
                print('Opening Marks')
            case 3:
                print('Opening Attendance')
            case 4:
                print('Opening Courses')
            case _:
                print('Invalid Choice')     
    case 2:
        teacher_choice = int(input('---Teacher Menu---\n1.Student\n2.Enter Marks\n3.Attendance\n4.Courses\n: '))
        match teacher_choice:
            case 1:
                print('Opening Students List')
            case 2:
                print('Opening Marks Entering Page')
            case 3:
                print('Opening Attendance Page')
            case 4:
                print('Opening Courses')
            case _:
                print('Invalid Choice')     
    case 3:
        admin_choice=int(input('---Admin Menu---\n1.Fees\n2.Admissions\n3.Notices\n4.Departments\n: '))
        match admin_choice:
            case 1:
                print('Opening Fee Management Portal')
            case 2:
                print('Opening Admission Management Portal')
            case 3:
                print('Opening Notice Mangement Portal')
            case 4:
                print('Opening Department Management Portal')
            case _:
                print('Invalid Choice')   
                
    case _:
        print('Invalid Choice')        
























































































# marks = int(input('Enter Your Marks: '))

# match marks:
#     case marks if marks >=90:
#         print('A')
#     case marks if marks >=80:
#         print('B')
#     case marks if marks >=70:
#         print('C')
#     case marks if marks >=60:
#         print('D')
#     case marks if marks >=50:
#         print('E')
#     case marks if marks <50:
#         print('F')
        

