print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a cross road. Where do you want to go? \n "
                "Type 'left' or 'right': ").lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. '
                    'There is an island in the middle of the lake. \n    '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across. ').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
                        "There is a house with 3 doors.\n    "
                        "One red, one yellow and one blue. "
                        "Which colour do you choose? ")
        if choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You got eaten by beasts. Game Over.")
        elif choice3 == "red":
            print("You got burned by fire. Game Over.")
        else:
            print("Game Over.")
    else:
        print("You got attacked by angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")