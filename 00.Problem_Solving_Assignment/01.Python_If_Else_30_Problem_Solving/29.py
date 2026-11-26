a = int(input('Enter The First Number: '))
b = int(input('Enter The Second Number: '))
c = int(input('Enter The Third Number: '))

if (a < b and a > c) or (a > b and a < c):
	print(a)
elif (b < a and b > c) or (b > a and b < c):
	print(b)
else:
	print(c)


