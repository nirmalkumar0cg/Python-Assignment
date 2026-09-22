marks1 = int(input("Enter Your 1st Subject Marks:"))
marks2 = int(input("Enter Your 2nd Subject Marks:"))
marks3 = int(input("Enter Your 3rd Subject Marks:"))
all_marks = marks1+marks2+marks3
if marks1 < 35 or marks2 < 35 or marks3 < 35:
    print("Fail")
    if all_marks/3 >= 75 and all_marks<100:
        print("Distinction")
    elif all_marks/3 >= 60 and all_marks <= 74:
        print("First Class")
    elif all_marks/3 >= 50 and all_marks <=59:
        print("Second Class")
    elif all_marks/3 >=35 and all_marks <=49:
        print("Pass")
else:
    print("Enter A Valid Marks")