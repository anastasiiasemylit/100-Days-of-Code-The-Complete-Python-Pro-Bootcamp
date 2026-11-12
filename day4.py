import random
ROCK = "    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)"
PAPER = "    _______\n---'   ____)____\n          ______)\n          _______)\n         _______)\n---.__________)"
SCISSOR = "    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)"
OPTION = [ROCK, PAPER, SCISSOR]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choice = random.randint(0,2)
if your_choice >= 0 and your_choice <= 2:
    print(OPTION[your_choice])
print("Computer choice: \n", OPTION[computer_choice])


if your_choice > 2:
    print("You typed an invalid number, you lose!")
if your_choice == 0 and computer_choice == 2:
    print("You win!")
elif your_choice == 1 and computer_choice == 0:
    print("You win!")
elif your_choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("You lose!")