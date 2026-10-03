# Q38. Smart Vehicle Dashboard
# Create a vehicle dashboard.

# Main options:

# 1 → Engine
# 2 → Lights
# 3 → Music
# 4 → Navigation
# For Engine:

# 1 → Start
# 2 → Stop
# For Lights:

# 1 → Headlights
# 2 → Indicators
# 3 → Hazard Lights
# For Music:

# 1 → Play
# 2 → Pause
# 3 → Next
# 4 → Previous
# For Navigation:

# 1 → Start Navigation
# 2 → Stop Navigation
# Use nested match-case.

dashboard = int(input('----Smart Vehicle Dashboard----\n1.Engine\n2.Lights\n3.Music\n4.Navigation\n: '))

match dashboard:
    case 1:
        engine = int(input('----Engine----\n1.Start\n2.Stop\n: '))
        match engine:
            case 1:
                print("Engine Started")
            case 2:
                print("Engine Stopped")
    case 2:
        lights= int(input('----Lights----\n1.Headlights\n2.Indicators\n3.Hazard Lights\n: '))
        match lights:
            case 1:
                print("Headlights Turned On")
            case 2:
                print("Indicators Turned On")
            case 3:
                print("Hazard Lights Turned On")
    case 3:
        music = int(input('----Music----\n1.Play\n2.Pause\n3.Next\n4.Previous\n: '))
        match music:
            case 1:
                print("Music Playing")
            case 2:
                print("Music Paused")
            case 3:
                print("Next Track Playing")
            case 4:
                print("Previous Track Playing")
    case 4:
        navigation = int(input('----Navigation----\n1.Start Navigation\n2.Stop Navigation\n: '))
        match navigation:
            case 1:
                print("Navigation Started")
            case 2:
                print("Navigation Stopped")