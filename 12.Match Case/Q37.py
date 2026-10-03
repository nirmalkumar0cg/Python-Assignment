# Q37. Online Learning Platform
# Create an online learning platform.

# First select:

# 1 → Programming
# 2 → Mathematics
# 3 → Communication
# Programming:

# 1 → Python
# 2 → Java
# 3 → C++
# Mathematics:

# 1 → Algebra
# 2 → Calculus
# 3 → Statistics
# Communication:

# 1 → English
# 2 → Presentation
# 3 → Interview Skills
# Use nested match-case.

subject = int(input('----Online Learning Platform----\n1.Programming\n2.Mathematics\n3.Communication\n: '))

match subject:
    case 1:
        option = int(input('----Programming Options----\n1.Python\n2.Java\n3.C++\n: '))
        match option:
            case 1:
                print("Python course selected")
            case 2:
                print("Java course selected")
            case 3:
                print("C++ course selected")
    case 2:
        option = int(input('----Mathematics Options----\n1.Algebra\n2.Calculus\n3.Statistics\n: '))
        match option:
            case 1:
                print("Algebra course selected")
            case 2:
                print("Calculus course selected")
            case 3:
                print("Statistics course selected")
    case 3:
        option = int(input('----Communication Options----\n1.English\n2.Presentation\n3.Interview Skills\n: '))
        match option:
            case 1:
                print("English course selected")
            case 2:
                print("Presentation course selected")
            case 3:
                print("Interview Skills course selected")