tri_side1 = int(input("Enter The First Side:"))
tri_side2 = int(input("Enter The Second Side:"))
tri_side3= int(input("Enter The Third Side:"))
if tri_side1 + tri_side2 > tri_side3:
    if tri_side1 + tri_side3 > tri_side2:
        if tri_side2+tri_side3 > tri_side1:
            print("Valid Triangle")
            if tri_side1==tri_side2==tri_side3:
                print("Equilateral")
            elif tri_side1==tri_side2 or tri_side1==tri_side3 or tri_side2==tri_side3:
                print("Isosceles")
            else:
                print("All Side's Are Different")
else:
    print("Invalid Triangle")
