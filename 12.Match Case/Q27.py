# Q27. Hospital Department Selection
# Create a hospital department menu:

# 1 → General Medicine
# 2 → Cardiology
# 3 → Orthopedics
# 4 → Pediatrics
# 5 → Emergency
# Display the selected department.

# For invalid input, display:

# Invalid Department

choice = int(input("""---Select Department---
                   1.General Medicince
                   2.Cardiology
                   3.Orthopedics
                   4.Pediatrics
                   5.Emergency"""))

match choice:
    case 1:
        print('General Medicince Selected')
    case 2:
        print('Cardiology Selected')
    case 3:
        print('Orthopedics Selected')
    case 4:
        print('Pediatrics Selected')
    case 5:
        print('Emergency Selected')
    case _:
        print('Invalid Department')