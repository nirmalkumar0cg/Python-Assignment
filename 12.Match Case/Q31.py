# Q31. Banking Application with Nested Menu
# Create a banking application.

# Main menu:

# 1 → Personal Banking
# 2 → Business Banking
# Personal Banking:

# 1 → Balance
# 2 → Transfer
# 3 → Loan
# Business Banking:

# 1 → Balance
# 2 → Payroll
# 3 → Business Loan
# Use nested match-case.

# Sample Input
# Enter banking type: 2
# Enter option: 3
# Sample Output
# Business Loan Selected

choice = int(input('----Banking Application----\n1.Personal Banking\n2.Business Banking\n: '))

match choice:
    case 1:
        option = int(input('----Personal Banking----\n1.Balance\n2.Transfer\n3.Loan\n: '))
        match option:
            case 1:
                print("Viewing Balance")
            case 2:
                print("Transfer Selected")
            case 3:
                print("Loan Selected")
    case 2:
        option = int(input('----Business Banking----\n1.Balance\n2.Payroll\n3.Business Loan\n: '))
        match option:
            case 1:
                print("Viewing Balance")
            case 2:
                print("Payroll Selected")
            case 3:
                print("Business Loan Selected")