import random


def play_game():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    while player_choice not in options:
        player_choice = input("Invalid choice. Enter a valid choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(options)
    print(f"Player : {player_choice}")
    print(f"Computer : {computer_choice}")
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or (
            player_choice == "paper" and computer_choice == "rock") or (
            player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")


playing = True
while playing:
    play_game()
    if input("Play again? (y/n): ").lower() == "n":
        playing = False
print("Thanks for playing!")
