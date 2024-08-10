import random

while True:
    user = input("Enter rock, paper, or scissors: ").lower()
    computer = random.choice(["rock", "paper", "scissors"])

    print(f"\nYou chose {user}, computer chose {computer}.\n")

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose.")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break