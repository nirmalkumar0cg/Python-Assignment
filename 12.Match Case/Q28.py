# Q28. Railway Ticket System
# Create a railway ticket menu:

# 1 → Book Ticket
# 2 → Cancel Ticket
# 3 → Check PNR
# 4 → Train Schedule
# 5 → Exit
# Display the appropriate action.

choice = int(input("""---Railway Ticket Menu---
                   1.Book Ticket
                   2.Cancel Ticket
                   3.Check PNR
                   4.Train Schedule
                   5.Exit
                   : """))

match choice:
    case 1:
        print("Ticket booked successfully.")
    case 2:
        print("Ticket canceled.")
    case 3:
        pnr = input("Enter PNR number: ")
        print("PNR Status: Confirmed")
    case 4:
        print("Train Schedule:")
        
    case 5:
        print("Exiting...")
    case _:
        print("Invalid choice.")