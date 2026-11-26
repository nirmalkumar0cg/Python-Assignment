# 12. Practice Problems
# Beginner
# Create a function with a local variable city and print it.

# def func():
#     city = 'kalol'
#     print(city)
# func()

# Create a global variable school. Read it inside a function.
# school = 'NEHS'
# def func():
#     print(school)
# func()

# Assign a variable inside an if block and print it outside the block.

# if 2>1:
#     huh = 'fkjh'
# print(huh)

# Use a for loop to assign a loop variable. Print it after the loop.
# loop = 'hhh'
# for x in loop:
#     pass
# print(x)

# Explain the difference between scope and lifetime in your own words.
# Intermediate
# Predict the output:

# value = 100
# def test():
#     value = 200
#     print(value)
# test()
# print(value)

#OUTPUT: 200 100

# Fix this code so it increments the global variable:

# clicks = 0
# def click():
#     clicks += 1

#ANSWER-:
# clicks = 0
# def click():
#     global clicks
#     clicks += 1
#     print(clicks)
# click()
# Explain why this code raises an error:


# name = "Asha"
# def show():
#     print(name)
#     name = "Ravi"
# show()
#REASON: It knows name variable exsists but it cannot access the data stored in it it's empty

# Write a nested function that reads a variable from its enclosing function.

# def outer():
#     city = 'kalol'
#     def inner():
#         nonlocal city
#         print(city)
#     inner()
# outer()

# Write a function that returns a list. Show that the returned list can be changed by the caller.

# def listfunc():
#     return ['abhimanu','krish','gayatri']

# my_list = listfunc()
# print(my_list)

# my_list.append('govind')
# print(my_list)

# Challenging
# Use nonlocal to create a counter that returns 1, 2, 3 across three calls.

# def counter():
#     count = 0
#     def countt():
#         nonlocal count
#         count+=1
#         return count
#     return countt
    
# r_count= counter()
# print(r_count())
# print(r_count())
# print(r_count())

# Predict the output:
# x = 1


# def outer():
#     x = 2

#     def inner():
#         x = 3
#         print(x)

#     inner()
#     print(x)


# outer()
# print(x)

# # 3
# # 2
# # 1


# Explain why the loop variable in a normal for loop can remain available after the loop, but a list-comprehension variable in Python 3 does not overwrite an outer variable.



# Create a function that returns another function. Explain which variable remains available and why.
# x=0 #global
# def outer():
#     x = 1 #nonlocal/enclosing
#     print(x)
#     def inner():
#         x=2 #local
#         return x
#     return inner()
# print(outer())
        

# Explain why variable names such as list, str, and sum should usually be avoided.