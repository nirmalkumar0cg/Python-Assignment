units = int(input("Enter the total units consumed: "))
if units <= 100:
    print(f"Total: {units*5}")
elif units <= 200:
    first100unit= units*5
    remainingunits = (units-100)*7
    print(f"Total:{first100unit+remainingunits}")
else:
    first100unit = units*5
    next100units = units*7
    remainingunits = (units-200)*10
    print(f"total:{first100unit+next100units+remainingunits}")
