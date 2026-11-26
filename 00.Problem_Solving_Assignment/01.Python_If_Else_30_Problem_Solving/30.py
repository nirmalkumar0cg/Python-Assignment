# 30. Complete Scholarship Decision ⭐
# Take:

# Student age
# Marks
# Family income
# Attendance percentage
# Scholarship requirements:

# Age:             18–25
# Marks:           85 or above
# Attendance:      75% or above
# Family income:   ₹300000 or below
# The student gets the scholarship only when all conditions are satisfied.

# Example
# Age: 20
# Marks: 90
# Income: 250000
# Attendance: 85

# Output:
# Scholarship Approved
# Another example:

# Age: 20
# Marks: 78
# Income: 250000
# Attendance: 82

# Output:
# Scholarship Rejected
# Reason: Marks below 85
# Extra Challenge
# If multiple conditions fail, print the reason for each failed condition.

# student_age = int(input('Enter The Age: '))
# marks = int(input('Enter The Marks: '))
# family_income = int(input('Enter Your Family Income: '))
# attendance_percentage = int(input('Enter Your Attendance Percentage: '))

# if student_age >= 18 and student_age <= 25:
#     if marks >= 85:
#         if family_income <= 300000:
#             print('Scholarship Approved')
#         else:
#             print('Scholarship Rejected')
#             print('Reason: Family Income Above 300000')
#     else:
#         print('Scholarship Rejected')
#         print('Reason: Marks Below 85')
# else:
#     print('Scholarship Rejected')
#     print('Reason: Age is not between 18-25')
    
            
        
    