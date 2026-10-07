import random

print("Welcome to Rock Paper Scissors!")

# Get a valid choice from the player
def get_player_choice():
    choice = input("Enter rock, paper, or scissors: ").lower()

    while choice != "rock" and choice != "paper" and choice != "scissors":
        print("That is not a valid choice.")
        choice = input("Enter rock, paper, or scissors: ").lower()

    return choice


# Compare the player and computer choices
def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif player == "rock" and computer == "scissors":
        return "win"
    elif player == "paper" and computer == "rock":
        return "win"
    elif player == "scissors" and computer == "paper":
        return "win"
    else:
        return "loss"


rounds = int(input("How many rounds would you like to play: "))

while rounds % 2 == 0:
    rounds = int(input("Please enter an odd number: "))

player_wins = 0
computer_wins = 0
rounds_played = 0

while rounds_played < rounds:
    player = get_player_choice()
    computer = random.choice(["rock", "paper", "scissors"])

    print(f"The computer chose {computer}.")

    result = determine_winner(player, computer)

    if result == "win":
        print("You won!")
        player_wins += 1
        rounds_played += 1
    elif result == "loss":
        print("You lost!")
        computer_wins += 1
        rounds_played += 1
    else:
        print("Tie! Play again.")

print("------------------------")
print(f"Score - You: {player_wins} | Computer: {computer_wins}")

if player_wins > computer_wins:
    print("You win!!!")
else:
    print("Computer wins!")

print("Thanks for playing!")