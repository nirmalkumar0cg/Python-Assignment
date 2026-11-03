# Take marks of 10 students using a for loop.

# For each student:

# Print "Fail" if marks are below 35.
# Print "Pass" for 35–49.
# Print "Good" for 50–74.
# Print "Excellent" for 75–100.
# At the end, print the number of students in each category.
for i in range(10):
    student_marks=int(input("Enter The Marks: "))
    if student_marks < 35:
        print("Fail")
    elif student_marks >= 35 and student_marks <= 49:
        print("Pass")
    elif student_marks >= 50 and student_marks <= 74:
        print("Good")
    else:
        print("Excellent")