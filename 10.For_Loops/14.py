user_int=int(input("Enter A Number:"))
for i in range(1,user_int,2):
    if i % 2 == 0 and i % 3 == 0:
        print(f"{i}")