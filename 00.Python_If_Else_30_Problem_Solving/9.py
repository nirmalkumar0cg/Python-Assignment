user_marks = int(input("Enter Your Marks: "))
if 90 <= user_marks <= 100:
    print("A")
elif 80 <= user_marks <= 89:
    print("B")
elif 70 <= user_marks <= 79:
    print("C")
elif 60 <= user_marks <= 69:
    print("D")
elif 40 <= user_marks <= 59:
    print("E")
else:
    print("Fail")