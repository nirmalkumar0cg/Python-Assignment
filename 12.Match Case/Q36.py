# Q36. Digital Payment Application
# Create a digital payment application.

# Payment type:

# 1 → UPI
# 2 → Card
# 3 → Wallet
# If UPI is selected:

# 1 → Scan QR
# 2 → Enter UPI ID
# If Card is selected:

# 1 → Credit Card
# 2 → Debit Card
# If Wallet is selected:

# 1 → Add Money
# 2 → Pay Using Wallet
# Use nested match-case.

payment_type = int(input('----Digital Payment Application----\n1.UPI\n2.Card\n3.Wallet\n: '))

match payment_type:
    case 1:
        upi = int(input('----UPI Options----\n1.Scan QR\n2.Enter UPI ID\n: '))
        match upi:
            case 1:
                print("Scanning QR code")
            case 2:
                print("Entering UPI ID")
            case _:
                print('Invalid Choice')
    case 2:
        card = int(input('----Card Options----\n1.Credit Card\n2.Debit Card\n: '))
        match card:
            case 1:
                print("Using Credit Card")
            case 2:
                print("Using Debit Card")
            case _:
                print('Invalid Choice')
    case 3:
        wallet = int(input('----Wallet Options----\n1.Add Money\n2.Pay Using Wallet\n: '))
        match wallet:
            case 1:
                print("Adding money to wallet")
            case 2:
                print("Paying using wallet")
            case _:
                print('Invalid Choice')
    case _:
        print('Invalid Choice')