# Problem 1
# Print numbers from 1 to 10, but stop when the number becomes 6.

# Expected output:

# 1
# 2
# 3
# 4
# 5

# for i in range(1,10):
#     if i==6:
#         break
#     print(i)

# Problem 2
# Given:

# numbers = [10, 20, 30, 40, 50]
# Search for 30.

# Once found, print:

# Found
# and stop the loop.

# numbers = [10, 20, 30, 40, 50]

# for i in range(0,len(numbers)):
#     if numbers[i]==30:
#         print('Found')
#         break

# Problem 3
# Take numbers from the user continuously.

# Stop when the user enters 0.
# user_num = int(input('Enter Number: '))
# while user_num != 0:
#     user_num = int(input('Enter Number: '))
#     if user_num == 0:
#         break

# Problem 4
# Print numbers from 1 to 100, but stop when you reach the first number divisible by 17.

# for i in range(1,101):
#     if i%17==0:
#         break
#     else:
#         print(i)

# 32. Practice Problems: continue
# Problem 1
# Print numbers from 1 to 20, but skip all even numbers.

# Expected output:

# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19

# for i in range(1,21):
#     if i%2==0:
#         continue
#     else:
#         print(i)

# Problem 2
# Given:

# numbers = [10, -2, 30, -5, 40, -8]
# Print only positive numbers using continue.

# Expected output:

# 10
# 30

# numbers = [10, -2, 30, -5, 40, -8]


# for i in range(0,len(numbers)):
#     if numbers[i]>0:
#         print(numbers[i])
#         continue
    
# Problem 3
# Print numbers from 1 to 20.

# Skip numbers divisible by 3.

# for i in range(1,21):
#     if i%3==0:
#         continue
#     print(i)
        
# Problem 4
# Given:

# numbers = [5, 12, 8, 21, 30, 7]
# Print only numbers greater than 10.

# Use continue.

# numbers = [5, 12, 8, 21, 30, 7]

# for i in range(0,len(numbers)):
#     if numbers[i]>10:
#         print(numbers[i])
#         continue

# Problem 3
# Write a program that checks whether a number is positive.

# For now, leave the positive case empty using pass.

# user_input = int(input('Enter Your Number: '))

# if user_input %2==0:
#     pass
# else:
#     print('not positive')

# 35. Challenge Problems
# Challenge 1
# Write a program that keeps asking the user for numbers.

# Rules:

# Positive number → print it.
# Negative number → skip it using continue.
# 0 → stop using break.

# user_input=int(input('Enter A Number: '))
# while user_input!=0:
#     user_input=(int(input('Enter A Number: ')))
#     if user_input == 0:
#         break
#     elif user_input > 0:
#         print(user_input)
#     elif user_input < 0:
#         continue

# Challenge 2
# Given:

# numbers = [12, 5, -4, 18, 0, 25, 30]
# Process the list using these rules:

# Negative number → skip.
# 0 → stop.
# Positive number → print.
# Expected output:

# 12
# 5
# 18

# numbers = [12, 5, -4, 18, 0, 25, 30]

# for i in range(0,len(numbers)):
#     if numbers[i]==0:
#         break
#     elif numbers[i]<0:
#         continue
#     else:
#         print(numbers[i])

# Challenge 3
# Write a program that searches for a number in a list.

# If found:

# Number found
# If the loop finishes without finding it:

# Number not found
# Hint: Use break and loop else.


# List=[1,2,3,4,5,6,7,8,9]
# user_input=int(input('Enter A Number You Want To Search In The List: '))

# for i in range(0,len(List)):
#     if List[i]==user_input:
#         print('Found')
#         break
# else:
#     if List[i]!=user_input:
#         print('Not Found')

# 34. Mixed Practice Problems
# Problem 1
# What is the output?

# for i in range(1, 6):
#     if i == 3:
#         break

#     print(i)

#Output- 1 2


# Problem 2
# What is the output?

# for i in range(1, 6):
#     if i == 3:
#         continue

#     print(i)

#Output-1 2 4 5


# Problem 3
# What is the output?

# for i in range(1, 6):
#     if i == 3:
#         pass

#     print(i)

#Output-1 2 3 4 5


# Problem 4
# What happens in this program?

# i = 1

# while i <= 5:
#     if i == 3:
#         continue

#     print(i)
#     i += 1

#Output- Infinite Loop


# Problem 5
# What is the output?

# for i in range(1, 5):
#     if i == 2:
#         pass
#     elif i == 3:
#         continue
#     elif i == 4:
#         break

#     print(i)

#Output- 1 2 4

# Problem 6
# What is the output?

# for i in range(1, 6):
#     if i == 3:
#         break
# else:
#     print("Done")

#Output-Nothing Will Be Printed


# Problem 7
# What is the output?

# for i in range(1, 6):
#     if i == 3:
#         continue
# else:
#     print("Done")

#Output-Done