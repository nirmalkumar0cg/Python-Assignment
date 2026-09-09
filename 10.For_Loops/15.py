user_int=int(input("Enter A Number:"))
count = 0
for i in range(1,user_int+1):
    if i % 2 == 0:
     count=count+1
print(f"{count}")
