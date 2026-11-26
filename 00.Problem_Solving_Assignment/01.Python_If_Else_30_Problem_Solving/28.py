name1 = input("Enter The Name Of 1st Person:")
age1 = int(input("Enter The Age Of 1st Person:"))
name2 = input("Enter The Name Of 2nd Person:")
age2 = int(input("Enter The Age Of 2nd Person:"))
name3 = input("Enter The Name Of 3rd Person:")
age3 = int(input("Enter The Age Of 3rd Person:"))
if age1 < age2 and age1 < age3 :
    print(name1,'is the youngest')
if age2 < age1 and age2 < age3:
    print(name2, 'is the youngest')
if age3 < age1 and age3 < age2:
    print(name3,'is the youngest')