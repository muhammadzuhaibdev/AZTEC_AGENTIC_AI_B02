#  Write a program that asks the user to input either 1 (turn on) or 0 (turn off).

userInput = int(input("Enter a number either 0 or 1: "))

match userInput:
    case 0:
        print("The light is off.")
    case 1:
        print("The light is on.")
    case _:
        print("Invalid Input")
















weekDay = input("Enter your week day: ")

match weekDay:
    case 'sunday':
        print(0)
    case 'monday':
        print(1)
    case 'tuesday':
        print(2)
    case 'wednesday':
        print(3)
    case 'thursday':
        print(4)
    case 'friday':
        print(5)
    case 'saturday':
        print(6)
        
    case _:
        print("Invalid Input")