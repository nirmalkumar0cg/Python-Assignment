# Q1. Number Pair Generator
# Print all pairs (i, j) where both values range from 1 to 3.

# Test Case
# Input: No input

# Expected Output:
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)

# Q2. Multiplication Pair
# Take N and print the multiplication result for every pair from 1 to N.

# Test Case
# Input: 3

# Expected Output:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 2 x 1 = 2
# 2 x 2 = 4"
# 2 x 3 = 6
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9


# n = int(input('Enter The Range'))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,'x',j,'=',i*j)

# Q3. Repeated Character Grid
# Take a character, rows and columns. Print the character as a rectangle.

# Test Case
# Input: `*`, rows=3, columns=4

# Expected Output:
# ****
# ****
# ****

# for i in range(1,4):
#     print('*',end='')
#     for j in range(1,5):
#         print('*',end='')
#     print(
    

# Q4. Coordinate Grid
# Take rows and columns and print every coordinate.

# Test Case
# Input: rows=2, columns=3

# Expected Output:
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)

# row = int(input("ENTER THE AMOUNT OF ROW'S: "))
# col = int(input("ENTER THE AMOUNT OF COL'S: "))

# for i in range(0,row):
#     for j in range(0,col):
#         print(f'{i,j}',end='')
#     print()

# Q5. Row Number Pattern
# Take N and print the row number N times in each row.

# Test Case
# Input: 4

# Expected Output:
# 1111
# 2222
# 3333
# 4444

# n = 4

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end='')
#     print()

# Q6. Column Number Pattern
# Take N and print 1 to N in every row.

# Test Case
# Input: 4

# Expected Output:
# 1234
# 1234
# 1234
# 1234
    
# n = 4

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end='')
#     print()


# Q7. Increasing Number Grid
# Take N and print 1, then 12, then 123, and so on.

# Test Case
# Input: 4

# Expected Output:
# 1
# 12
# 123
# 1234

# n = 4

# for i in range(n):
#     for j in range(1,i+2):
#        print(j,end='') 
#     print()

# Q8. Decreasing Number Grid
# Take N and print 1..N, then one fewer number on every row.

# Test Case
# Input: 4

# Expected Output:
# 1234
# 123
# 12
# 1

# n = 4

# for i in range(n):
#     for j in range(1,n+1-i):
#         print(j,end='')
#     print()

# Q9. Star Rectangle
# Take rows and columns and print a rectangle of *.

# Test Case
# Input: rows=3, columns=5

# Expected Output:
# *****
# *****
# *****

# row= int(input('Enter The Rows: '))
# col= int(input('Enter The Columns: '))

# for i in range(row):
#     for j in range(col):
#         print('*',end='')
#     print()


# 10. Alternating 0 and 1
# Take N and print an N×N grid where columns alternate between 0 and 1.

# Test Case
# Input: 4

# Expected Output:
# 0101
# 0101
# 0101
# 0101

# n = 4

# for i in range(n):
#     for j in range(n):
#         if j % 2 == 0:
#             print(0,end='')
#         else:
#             print(1,end='')
#     print()

# Level 2 — Conditions Inside Nested Loops
# Q11. Even Number Grid
# Print only even column values for every row.

# Test Case
# Input: rows=3, columns=6

# Expected Output:
# 2 4 6
# 2 4 6
# 2 4 6

# rows=3
# cols=6

# for i in range(rows):
#     for j in range(1,cols+1):
#         if j % 2 == 0:
#             print(j,end=' ')
#     print()
    
# Q12. Odd Number Grid
# Print odd numbers from 1 to N in every row.

# Test Case
# Input: N=7

# Expected Output:
# 1 3 5 7
# 1 3 5 7
# 1 3 5 7
# 1 3 5 7
# 1 3 5 7
# 1 3 5 7
# 1 3 5 7

# n = 7

# for i in range(n):
#     for j in range(n+2):
#         if j % 2 == 1:
#             print(j,end=' ')
#     print()

# Q13. Even-Odd Classification
# For i and j from 1 to 4, print E when i+j is even, otherwise O.

# Test Case
# Input: No input

# Expected Output:
# E O E O
# O E O E
# E O E O
# O E O E

# for i in range(5):
#     for j in range(4):
#         a = i+j
#         if a % 2 == 0:
#             print('E',end=' ')
#         else:
#             print('O',end=' ')
#     print()

# Q14. Equal Coordinate Detector
# For every pair from 1 to 5, print Same when i==j, otherwise Different.

# Test Case
# Input: N=3

# Expected Output:
# Same Different Different
# Different Same Different
# Different Different Same

# n = 3

# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print('same',end=' ')
#         else:
#             print('Different',end=' ')
#     print()


# Q15. Diagonal Values
# Create an N×N grid with 1 on the main diagonal and 0 elsewhere.

# Test Case
# Input: N=4

# Expected Output:
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

# n=4
# count = 0

# for i in range(n):
#     count+=1
#     for j in range(1,n+1):
#         if j==count:
#             print(1,end=' ')
#         else:
#             print(0,end=' ')
#     print()

# Q16. Number Divisibility Grid
# For i,j from 1 to 5, print X if i is divisible by j, otherwise -.

# Test Case
# Input: No input

# Expected Output:
# X - - - -
# X X - - -
# X - X - -
# X X - X -
# X - - - X


# for i in range(1,6):
#     for j in range(1,6):
#         if i%j==0:
#             print('X',end=' ')
#         else:
#             print('-',end=' ')
#     print()

# 17. Multiples Detector
# For every i from 1 to N, print values j from 1 to N that are multiples of i.

# Test Case
# Input: N=4

# Expected Output:
# 1 2 3 4
# 2 4
# 3
# 4

# n=4

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j%i==0:
#             print(j,end=' ')
#         else:
#             print('',end='')
#     print()
    
# Q18. Pair Sum Filter
# Print all pairs from 1 to N whose sum is greater than N.

# Test Case
# Input: N=4

# Expected Output:
# 1 4
# 2 3
# 2 4
# 3 2
# 3 3
# 3 4
# 4 1
# 4 2
# 4 3
# 4 4

# n = 4

# for i in range(n+1):
#     for j in range(n+1):
#         if i+j>n:
#             print(i,j)
            
# Q19. Pair Product Filter
# Print pairs and products only when the product is even.

# Test Case
# Input: N=3

# Expected Output:
# 1 2 2
# 2 1 2
# 2 2 4
# 2 3 6
# 3 2 6

# n=3

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if (i*j)%2==0:
#             print(i,j,i*j)
# print()

# Q20. Special Coordinate
# Print SPECIAL for i==j, PAIR for i+j==N, otherwise NORMAL. Decide condition priority carefully.

# Test Case
# Input: N=4

# Expected Output: A 4×4 classification grid; diagonal positions are SPECIAL and remaining sum-4 positions are PAIR.

# n = 4

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print('SPECIAL',end=' ')
#         elif i+j==n:
#             print('PAIR',end=' ')
#         else:
#             print('NORMAL',end=' ')
#     print()

# Level 3 — Strings + Nested Loops
# Q21. Character Repetition
# For every character, print it three times.

# Test Case
# Input: `CAT`

# Expected Output:
# CCC
# AAA
# TTT

# inputiya = 'CAT'
# for i in range(len(inputiya)):
#     for j in range(len(inputiya)):
#         print(inputiya[i],end='')
#     print()
    

# Q22. Character with Position
# For every character, print it with repetition numbers 0,1,2.

# Test Case
# Input: `AB`

# Expected Output:
# A 0
# A 1
# A 2
# B 0
# B 1
# B 2

# inputiya = 'AB'

# for i in range(len(inputiya)):
#     for j in range(len(inputiya)+1):
#         print(inputiya[i],j)

# Q23. Compare Every Character
# Compare every character with every other character and label Same/Different.

# Test Case
# Input: `AB`

# Expected Output: A/A is Same; all other ordered pairs are Different.

# user_input = input('Enter The Words: ')
# for i in user_input:
#     for j in user_input:
#         if i==j:
#             print(i,'/',j,'is same')
#         else:
#             print(i,'/',j,'different')

# Q24. Character Matching
# Compare every character of two strings and print equal pairs.

# Test Case
# Input: `ABC` and `BCD`

# Expected Output:
# B B
# C C

# user_input = 'ABC'
# user_input1 = 'BCD'

# for i in user_input:
#     for j in user_input1:
#         if i==j:
#             print(i,j)

# Q25. Count Matching Characters
# Count equal character comparisons between two strings without using count().

# Test Case
# Input: `ABC` and `BCD`

# Expected Output:
# 2

# user_input = 'ABC'
# user_input1 = 'BCD'
# count=0
# for i in user_input:
#     for j in user_input1:
#         if i==j:
#             count+=1
# print(count)
    
    
# Q26. Character Frequency Without count()
# For each character, count its occurrences using nested loops.

# Test Case
# Input: `BANANA`

# Expected Output:
# B = 1
# A = 3
# N = 2

# user_input='BANANA'
# for i in range(0,len(user_input)):
#     count=0
#     if user_input[i] in user_input[:i]:
#         continue
#     for j in user_input:
#         if j == user_input[i]:
#             count+=1
#     print(user_input[i],'=',count)
    
# Q27. Vowel-Consonant Classification
# Compare each character against AEIOUaeiou using a nested loop.

# Test Case
# Input: `AbC`

# Expected Output:
# A = Vowel
# b = Consonant
# C = Consonant

# user_input = 'AbCCccCiI'
# vowel = 'AEIOUaeiou'

# for i in user_input:
#     if i in vowel:
#         print(i,'=','Vowel')
#     else:
#         print(i,'=','Consonant')

# Q28. Common Characters
# Print characters occurring in both strings without using set().

# Test Case
# Input: `HELLO` and `WORLD`

# Expected Output: Common characters include L and O.

# user_input = 'HELLO'
# user_input1 = 'WORLD'
# bag=''
# for i in user_input:
#     for j in user_input1:
#         if i in bag:
#             continue
#         if i == j:
#             bag+=i
#             print(i)
            
# Q29. Character Pair Generator
# Print every ordered pair of characters.

# Test Case
# Input: `ABC`

# Expected Output:
# A A
# A B
# A C
# B A
# B B
# B C
# C A
# C B
# C C
    
# user_input = 'ABC'

# for i in user_input:
#     for j in user_input:
#         print(i,j)
    
# Q30. Different Character Pairs
# Print ordered pairs whose positions are different.

# Test Case
# Input: `ABC`

# Expected Output: A B, A C, B A, B C, C A, C B.

# user_input = 'ABC'

# for i in user_input:
#     for j in user_input:
#         if i == j:
#             continue
#         else:
#             print(i,j,",",end=' ')
            
# Level 4 — Strings + Conditions + ASCII
# Q31. Same or Different Pair
# Print each character pair with Same/Different and the pair itself.

# Test Case
# Input: `AAB`

# Expected Output: Equal A/A is Same; all unequal pairs are Different.

# user_input = 'AAB'

# for i in user_input:
#     for j in user_input:
#         if i==j:
#             print(i,'/',j,'Is Same')
#         else:
#             print(i,'/',j,'Is Different')
            
# Q32. Vowel-Consonant Pair
# Print pairs where first character is vowel and second is consonant.

# Test Case
# Input: `ABEC`

# Expected Output: Pairs such as A-B, A-C, E-B, E-C.

# user_input='ABEC'

# vowel = 'AEIOUaeiou'



# for i in user_input:
#     for j in user_input:
#         if i in vowel and j not in vowel:
#             print(i,j)

# Q33. Same Case Pair
# Print pairs whose two characters have the same case.

# Test Case
# Input: `AbCD`

# Expected Output: Uppercase-uppercase and lowercase-lowercase pairs only.

# user_input = 'AbCD'
# upper = user_input.upper()
# lower = user_input.lower()
# for i in user_input:
#     for j in user_input:
#         if i in upper and j in upper:
#             print(i,j)
#         if i in lower and j in lower:
#             print(i,j)

# Q34. ASCII Difference
# For every pair, print the pair and absolute ASCII difference.

# Test Case
# Input: `ABC`

# Expected Output: A B -> 1, A C -> 2, B C -> 1, with reverse pairs as well.

# user_input = 'ABC'
# for i in user_input:
#     for j in user_input:
#         if i == j:
#             continue
#         print(i,j,'->',(abs(ord(i)-ord(j))),',',end=' ')


# Q35. ASCII Relationship
# Classify each pair as Increasing, Decreasing or Same by ASCII value.

# Test Case
# Input: `ABC`

# Expected Output: A→B Increasing, B→A Decreasing, A→A Same, etc.


# user_input = 'ABC'

# for i in user_input:
#     for j in user_input:
#         if ord(i)-ord(j)<0:
#             print(i,'->',j,'Increasing')
#         elif ord(i)-ord(j)>0:
#             print(i,'->',j,'Decreasing')
#         elif ord(i)-ord(j) == 0:
#             print(i,'->',j,'Same')


# Level 5 — split() + Nested Loops (SKIP)
# Q36. Compare Words
# Split a sentence and print every word pair.

# Test Case
# Input: `I love Python code`

# Expected Output: All ordered word pairs.

# user_input=input('Enter A Sentence: ').split()

# print(user_input)

# for i in range(len(user_input)):
#     for j in range(len(user_input)):
#         if user_input[i]==user_input[j]:
#             continue
#         print(user_input[i],user_input[j]) 

# Q37. Same-Length Word Pairs
# Print pairs of words having equal length.

# Test Case
# Input: `I love Python code`

# Expected Output:
# love code

# user_input=input('Enter A Sentence: ').split()

# print(user_input)

# for i in range(len(user_input)):
#     for j in range(len(user_input)):
#         if len(user_input[i])==len(user_input[j]):
#             print(user_input[i],user_input[j])

# Q38. Common Starting Character
# Print word pairs whose first characters match.

# Test Case
# Input: `cat car dog`

# Expected Output:
# cat car

# user_input = input('Enter The Words: ').split()
# for i in user_input:
#     for j in i:
#         if j == user_input[0][0]:
#             print(i)
            
# Q39. Common Ending Character
# Print word pairs whose final characters match.

# Test Case
# Input: `cat bat dog`

# Expected Output:
# cat bat

# user_input = ['cat','bat','dog']
# for i in user_input:
#     for j in i:
#         if j == user_input[0][-1]:
#             print(i)

# Q40. Word Character Match
# Print word pairs sharing at least one character; do not use set().

# Test Case
# Input: `apple pie orange`

# Expected Output: Matching word pairs.

# user_input = ['apple','pie','orange']

# for i in user_input:
#     for j in user_input:
#         for k in j:
#             if i == j:
#                 continue
#             else:
#                 if k in i:
#                     print(i,j)
#                     break
                    
# Q42. Longest and Shortest Word Pair
# Use nested loops to identify longest and shortest words without max/min.

# Test Case
# Input: `I love Python programming`

# Expected Output:
# Longest = programming
# Shortest = I

# user_input = ['I', 'love', 'python', 'programming']
# L = []
# longest = user_input[0]
# shortest = user_input[0]

# for i in user_input:
#     L.append(len(i))
    
# for i in range(len(L)):
#     for j in range(len(L)):
#         if i!=j:
#             if len(user_input[i])>len(longest):
#                 longest=user_input[i]
#             if len(user_input[i])<len(shortest):
#                 shortest=user_input[i]
                
# print(longest)
# print(shortest)


# Level 6 — Dynamic Nested Loops
# Q43. Growing Inner Loop
# For each i from 1 to N, run inner loop 1..i.

# Test Case
# Input: 4

# Expected Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4


# n=4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()
    
# Q44. Shrinking Inner Loop
# Decrease the inner-loop size each row.

# Test Case
# Input: 4

# Expected Output:
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# n=4
# for i in range(1,n+1):
#     for j in range(i+1,n+2):
#         print(j-i,end=' ')
#     print()

# Q45. Multiplication Triangle
# For row i, print i×1 through i×i.

# Test Case
# Input: 4

# Expected Output: Row 4 contains 4 8 12 16.

# n=4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i*j,end=' ')
#     print()

# Q46. Conditional Dynamic Loop
# Run inner loop i times and print only even inner values.

# Test Case
# Input: 4

# Expected Output: DOUBTTTTTT
# 2
# 2
# 2 4
# 2 4 6
    
# n=4
# for i in range(1,n+1):
#     for j in range(1,i*2):
#         if j%2==0:
#             print(j,end=' ')
#     print()

# For i=0..N-1, run range(i).

# Test Case
# Input: 4

# Expected Output: i=0 produces no inner output; later rows show 0, then 0 1, then 0 1 2.

# n = 4

# for i in range(n+1):
#     for j in range(i):
#         print(j,end=' ')
#     print()
    
# Q48. Reverse Dynamic Range
# For each i, print i down to 1.

# Test Case
# Input: 4

# Expected Output:
# 1
# 2 1
# 3 2 1
# 4 3 2 1
    
# n=4

# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j,end=' ')
#     print()

# Level 7 — Number Logic + Nested Loops
# Q49. Factors of Every Number
# Print all factors of every number from 1 to N.

# Test Case
# Input: 6

# Expected Output:
# 1 -> 1
# 2 -> 1 2
# 3 -> 1 3
# 4 -> 1 2 4
# 5 -> 1 5
# 6 -> 1 2 3 6


# n = 6

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i%j==0:
#             print(j,end=' ')
#     print()
    

# Q50. Perfect Number Detector
# Find perfect numbers up to N using divisor sums.

# Test Case
# Input: 30

# Expected Output:
# Perfect: 6, 28

# n = 30



















































































# _ = 1
# __ = [_]

# def _0_(_=_, __=__):
#     global __
#     ___ = __[0] if isinstance(__, list) else __
#     __ = [___ + 1]

#     def _O_(___=___):
#         nonlocal _
#         _ = _ + [___]
        
#         def _o_():
#             global _
#             nonlocal ___
#             ___ += _[-1]
#             _ = [___]
#             return ___
#         return _o_
#     return _O_

# f = _0_()
# g = _0_([2], 3)

# print(f()())
# print(g()())
# print(f()())















































































































































































































































































































































































































































































































































































































































































































































































# Q69. Diagonal Cross
# Print * on both diagonals.

# Test Case
# Input: 5

# Expected Output:
# *   *
#  * *
#   *
#  * *
# *   *

# n = 5

# for row in range(n):
#     for col in range(n):
#         if row == col or row+col == n-1:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()
