n = int(input("Enter The Number Of Rows You Want:"))
for row in range(1,n):
    for col in range(1, row+1):
        print(col,end="")
    print()