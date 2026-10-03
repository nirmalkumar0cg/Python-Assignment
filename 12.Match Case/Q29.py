# Q29. Library Management System
# Create a library menu:

# 1 → Search Book
# 2 → Issue Book
# 3 → Return Book
# 4 → View Issued Books
# 5 → Exit

choice = int(input("""---Library Menu---
                   1.Search Book
                   2.Issue Book
                     3.Return Book
                     4.View Issued Books
                     5.Exit
                     : """))

match choice:
    case 1:
        book_name = input("Enter the book name to search: ")
        print(f"Searching for '{book_name}'")
    case 2:
        book_name = input("Enter the book name to issue: ")
        print(f"Issuing '{book_name}'")
    case 3:
        book_name = input("Enter the book name to return: ")
        print(f"Returning '{book_name}'")
    case 4:
        print("Viewing issued books")
    case 5:
        print("Exiting")