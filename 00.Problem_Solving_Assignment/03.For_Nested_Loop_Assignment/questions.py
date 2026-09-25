# 1. Print a 3×3 Star Grid
# Write a Python program to print:

# * * *
# * * *
# * * *
# for row in range(3):
#     for col in range(3):
#         print('*',end=' ')
#     print()
    
# 2. Print Numbers in Rows
# Write a Python program to print:

# 1 2 3
# 1 2 3
# 1 2 3
# for row in range(3):
#     for col in range(1,4):
#         print(col,end=' ')
#     print()
# 3. Print Row Numbers
# Write a Python program to print:

# 1 1 1
# 2 2 2
# 3 3 3
# for row in range(1,4):
#     for col in range(3):
#         print(row,end=' ')
#     print()
# 4. Increasing Star Pattern
# Write a Python program to print:

# *
# * *
# * * *
# * * * *
# * * * * *

# for row in range (6):
#     for col in range(1,row+1):
#         print('*',end=' ')
#     print()
# 5. Decreasing Star Pattern
# Write a Python program to print:

# * * * * *
# * * * *
# * * *
# * *
# *

# n = 5
# for row in range (n): # 0 1 2 3 4
#     for col in range(row,n): # 0,5 ; 1,5 , 2,5 , 3,5 ,4,5 ,5,5
#         print('*',end=' ')
#     print()

# 6. Increasing Number Pattern
# Write a Python program to print:

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for row in range (1,6):
#     for col in range(1,row+1):
#         print(col,end=' ')
#     print()

    
# 7. Repeated Number Pattern
# Write a Python program to print:

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# for row in range (1,6):
#     for col in range(1,row+1):
#         print(row,end=' ')
#     print()
    
# 8. Multiplication Tables from 1 to 5
# Write a Python program to print multiplication tables from 1 to 5.

# Each table should contain multiplication from 1 to 10.

# for row in range(1,4):
#     for col in range(1,11):
#         print(row*col,end=' ')
#     print()

# 9. Multiplication Grid
# Write a Python program to print:

# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15

# n = int(input("Enter A Number: "))
# for row in range(1,n+1):
#     for col in range(1,6):
#         print(row*col,end=' ')
#     print()
    
# 10. Print Squares in Rows
# Write a Python program to print the squares of numbers from 1 to 5 in 5 rows.

# Expected pattern:

# 1 4 9 16 25
# 1 4 9 16 25
# 1 4 9 16 25
# 1 4 9 16 25
# 1 4 9 16 25

# n = int(input("Enter The Number: "))
# for row in range(n):
#     for col in range(1,n+1):
#         print(col*col,end=' ')
#     print()
    
# 11. Alphabet Pattern
# Write a Python program to print:

# A
# A B
# A B C
# A B C D
# A B C D E

# alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for row in range(1,6):
#     for col in range(row):
#         print(alphabets[col],end=' ')
#     print()
    
# 12. Repeated Alphabet Pattern
# Write a Python program to print:

# A
# B B
# C C C
# D D D D
# E E E E E
# alphabets = 'ABCEDFGHIJKLMNOPQRSTUVWXYZ'
# for row in range(0,6):
#     for col in range(row+1):
#         print(alphabets[row],end=' ')
#     print()



# 13. Odd Number Pattern
# Write a Python program to print:

# 1
# 1 3
# 1 3 5
# 1 3 5 7
# 1 3 5 7 9

# for row in range(1, 6):
#     for col in range(1,row+1):
#         num = col*2-1
#         if num % 2 != 0:
#             print(num, end=' ')
#     print()
    
# 14. Even Number Pattern
# Write a Python program to print:

# 2
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10
#Yatra Logic
# n = 4
# for i in range(n+1):
#     for j in range(2*i+2):
#         if j % 2!=0:
#             print(j,end=' ')
#     print()

# for row in range(1,6):
#     for col in range(1,row+1):
#         num=col*2
#         if num % 2 == 0:
#             print(num,end=' ')
#     print()
# 15. 5×5 Star Square
# Write a Python program to print:

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# for row in range(5):
#     for col in range(5):
#         print('*',end=' ')
#     print()

# 16. 5×5 Number Square
# Write a Python program to print:

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# for row in range(5):
#     for col in range(1,6):
#         print(col,end=' ')
#     print()

# 17. Row-wise Numbers
# Write a Python program to print:

# 1 2 3
# 4 5 6
# 7 8 9

# for row in range(1,4):
#     for col in range(1,4):
#         if row == 1:
#             print(col,end=' ')
#         elif row ==2:
#             print(col+3,end=' ')
#         elif row ==3:
#             print(col+6,end=' ')
#     print()

    
