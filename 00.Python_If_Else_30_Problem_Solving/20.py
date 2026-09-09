tri_side1 = int(input("Enter The First Side:"))
tri_side2 = int(input("Enter The Second Side:"))
tri_side3= int(input("Enter The Third Side:"))
if tri_side1 + tri_side2 > tri_side3:
    if tri_side1 + tri_side3 > tri_side2:
        if tri_side2+tri_side3 > tri_side1:
            print("Valid Triangle")
else:
    print("Invalid Triangle")

