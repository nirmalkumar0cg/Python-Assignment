# def square(n):
#     return n*n

# print(square(5))

# square = lambda n:n*n
# print(square(5))

# multiply = lambda n,y:n*y
# print(multiply(5,6))

# cube = lambda n:n**3
# print(cube(2))

# checker = lambda n: 'Even' if n % 2 == 0 else 'Odd'
# print(checker(2))

# find_smallest = lambda n,y: y if y<n else n
# print(find_smallest(2,5))

# area_of_rectangle = lambda l,b : f"Area of rectangle=>{l*b}"
# print(area_of_rectangle(5,6)) 

# small_convert = lambda n: n.lower()
# print(small_convert('HELLO'))

# is_vowel = lambda n: 'Is Vowel' if n in 'aeiouAEIOU' else 'Is Not Vowel'
# print(is_vowel('z'))

# word = 'coding'
# upper_convert = lambda word:word.upper()
# print(upper_convert(word))

# word = 'coding'
# upper_convert = map(lambda c:c.upper(),word)
# print(''.join(upper_convert))

# word = 'programming'

# vowel_extract = filter(lambda j: j in 'aeiouAEIOU',word)

# print(''.join(vowel_extract))

def lab3(n):
    if n == 0:
        return
    lab3(n-1)
    print(n)

lab3(5)