import random

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    print("\n" *42)
    possible_actions = ["rock", "paper", "scissors"]
    user2_action = input("Enter a choice (rock, paper, scissors): ")
    print("\n" *42)
    print(f"\nPlayer 1 chose {user_action}, Player 2 chose {user2_action}.\n")

    if user_action == user2_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if user2_action == "scissors":
            print("Rock smashes scissors! Player 1 Won!")
        else:
            print("Paper covers rock! Player 2 Won!")
    elif user_action == "paper":
        if user2_action == "rock":
            print("Paper covers rock! Player 1 Won!")
        else:
            print("Scissors cuts paper! Player 2 Won!")
    elif user_action == "scissors":
        if user2_action == "paper":
            print("Scissors cuts paper! Player 1 Won!")
        else:
            print("Rock smashes scissors! Player 2 Won!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
