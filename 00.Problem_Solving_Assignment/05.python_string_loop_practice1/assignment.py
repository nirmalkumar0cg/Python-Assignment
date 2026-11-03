# Q1. Find the substring 420
# Description
# You are given an integer N. Your task is to check whether the string "420" is present in its decimal representation.

# Print "Caught" if "420" is present.
# Otherwise, print "Escaped".
# Input
# A single integer N.

# Constraints
# N < 1000000
# Output
# Print Caught or Escaped.

# Sample Input 1
# 97420
# Sample Output 1
# Caught
# Explanation
# The number 97420 contains the sequence 420, so the output is Caught.

# Sample Input 2
# 12345
# Sample Output 2
# Escaped

# n = int(input('Enter A Number: '))
# storage=str(n)

# for i in storage:
#     if '420' in storage:
#         print('Caught')
#         break
#     else:
#         print('Escaped')
#         break

# Q2. Decompress the string
# Description
# You are given a string containing lowercase English letters followed by integers.

# For every letter, the integer immediately following it tells you how many times that letter must appear in the output.

# For example:

# Input: a3b2
# a is followed by 3, so write a three times.
# b is followed by 2, so write b two times.
# Output: aaabb
# Assume every letter is followed by a positive single-digit integer.

# Input
# A single string.

# Constraints
# Length of the string is at most 100.
# The string contains lowercase English letters and digits.
# Every letter is followed by one digit from 1 to 9.
# Output
# Print the decompressed string.

# Sample Input 1
# a3b2
# Sample Output 1
# aaabb
# Sample Input 2
# c2d4
# Sample Output 2
# ccdddd

# n = input('Enter The String You Want To Decompress: ')
# nn = n.strip()
# newn=''
# num = ''
# for i in range(1):
#     num+=n[0::2].strip()
#     for j in range(1):
#         newn+=nn[0::2]

# for k in range(len(newn)):
#     print(newn[k]*int((num[k])))
     
# letters = n[0::2]
# digits = n[1::2]

# for i in range(len(letters)):
#     print(letters[i]*int(digits[i]))

# def decompression(a):
#     letters = a[0::2]
#     digits = a[1::2]
#     for i in range(len(letters)):
#         print(letters[i]*int(digits[i]))
        
# decompression('a2b4')

# Q3. Check whether both halves are palindromes
# Description
# You are given a string str and its length N. The value of N is always even.

# Divide the string into two equal halves:

# The first half contains characters from index 0 to N // 2 - 1.
# The second half contains characters from index N // 2 to N - 1.
# Check whether both halves are palindromes.

# A palindrome is a string that reads the same from left to right and right to left.

# Print yes if both halves are palindromes. Otherwise, print no.

# Input
# The first line contains an even integer N.
# The second line contains the string str.
# Constraints
# N is always even.
# The string contains only lowercase English letters.
# The length of the string is N.
# Output
# Print yes or no.

# Sample Input 1
# 6
# ababcb
# Sample Output 1
# yes
# Explanation
# The first half is aba, and the second half is bcb. Both are palindromes.

# Sample Input 2
# 4
# abdc
# Sample Output 2
# no
# Sample Input 3
# 6
# ababba
# Sample Output 3
# no
# Explanation
# The first half, aba, is a palindrome. The second half, bba, is not. Therefore, the answer is no.

# user_input=input('Enter The  String You Want to check the palindrome of: ')

# half_formula = int((len(user_input)/2))

# first_half = user_input[0:half_formula:]
# second_half = user_input[half_formula::]
# first_half_reverse = ''
# second_half_reverse = ''
# for i in range(len(first_half)-1,-1,-1):
#     first_half_reverse+=first_half[i]
# for j in range(len(second_half)-1,-1,-1):
#     second_half_reverse+=second_half[j]
    
# if first_half==first_half_reverse and second_half == second_half_reverse:
#     print('Both half are palindrome.')
# else:
#     print('No')


# Q4. Count a character in a string
# Description
# You are given a string S and a character C. Count how many times character C appears in S.

# The comparison is case-sensitive. For example, A and a are different characters.

# Input
# The first line contains the string S.
# The second line contains the character C.
# Constraints
# 1 <= length of S <= 100
# C contains exactly one character.
# Output
# Print the number of occurrences of C in S.

# Sample Input 1
# programming
# g
# Sample Output 1
# 2
# Sample Input 2
# banana
# a
# Sample Output 2
# 3

# user_word = input('Enter The Word: ')
# user_char = input('Enter The Char You Want to count in your word: ')
# count=0
# for i in range(len(user_word)):
#     if user_char in user_word[i]:
#         count+=1
# print(count)

# Q5. Reverse a string using a loop
# Description
# You are given a string S. Reverse the string without using slicing with a step of -1 and without using built-in reverse methods.

# Build the reversed string by visiting the characters using a loop.

# Input
# A single string S.

# Constraints
# 1 <= length of S <= 100
# The string contains English letters.
# Output
# Print the reversed string.

# Sample Input 1
# python
# Sample Output 1
# nohtyp
# Sample Input 2
# hello
# Sample Output 2
# olleh

# user_input= input('Enter The Word You Want To Reverse: ')
# reversed_user_input=''
# for i in range(len(user_input)-1,-1,-1):
#     reversed_user_input+=user_input[i]
# print(reversed_user_input)

# Q6. Check whether the complete string is a palindrome
# Description
# You are given a string S. Check whether the complete string is a palindrome.

# A palindrome reads the same from left to right and right to left.

# Print yes if the string is a palindrome. Otherwise, print no.

# Do not use slicing with a step of -1.

# Input
# A single lowercase string S.

# Constraints
# 1 <= length of S <= 100
# The string contains only lowercase English letters.
# Output
# Print yes or no.

# Sample Input 1
# madam
# Sample Output 1
# yes
# Sample Input 2
# coding
# Sample Output 2
# no


