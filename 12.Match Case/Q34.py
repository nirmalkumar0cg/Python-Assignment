# Q34. Gaming Console Menu
# Create a gaming console menu:

# 1 → Start Game
# 2 → Load Game
# 3 → Settings
# 4 → Exit
# If Settings is selected, show:

# 1 → Sound
# 2 → Graphics
# 3 → Controls
# Use nested match-case for the Settings menu.

choice = int(input('----Gaming Console Menu----\n1.Start Game\n2.Load Game\n3.Settings\n4.Exit\n: '))

match choice:
    case 1:
        print("Starting Game")
    case 2:
        print("Loading Game")
    case 3:
        setting = int(input('----Settings----\n1.Sound\n2.Graphics\n3.Controls\n: '))
        match setting:
            case 1:
                print("Sound settings selected")
            case 2:
                print("Graphics settings selected")
            case 3:
                print("Controls settings selected")
    case 4:
        print("Exiting Game")