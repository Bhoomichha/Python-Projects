import random

computer_win = 0
user_win = 0
tie = 0

options =["rock", "paper", "scissors"]

while True:
    user_choice = input("\nPlease enter Rock/Paper/Scissors or Q to quit: ").lower()
    if user_choice == 'q':
        break
    if user_choice not in options:
        print("Invalid input. Please enter Rock/Paper/Scissors or Q to quit")
        continue

    random_number = random.randint(0,2)
    # rock:0, paper:1, scissors:2
    computer_pick = options[random_number]
    print("\nComputer picked", computer_pick +".")

    if user_choice == "rock" and computer_pick == "scissors":
        print("You win!")
        user_win += 1
    elif user_choice == "paper" and computer_pick =="rock":
        print("You win!")
        user_win += 1
    elif user_choice == "scissors" and computer_pick == "paper":
        print("You win!")
        user_win += 1
    elif user_choice == "rock" and computer_pick == "rock":
        print("It's a tie!")
        tie += 1
    elif user_choice == "paper" and computer_pick == "paper":
        print("It's a tie!")
        tie += 1
    elif user_choice == "scissors" and computer_pick == "scissors":
        print("It's a tie!")
        tie += 1
    else:
        print("You lose!")
        computer_win += 1
print("")
print("Final Results:")
print("   You won", user_win, "times.\n   Computer won", computer_win, "times.")
print("  ",tie, "times was a tie.\n")
    
    