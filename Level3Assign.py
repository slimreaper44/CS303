import random


def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    Guesses = 0

    print("I'm thinking of a number between 1 and 100")

    while True:
        Guess = int(input("Enter your guess: "))

        #Make sure the guess is within the valid range
        if Guess < 1 or Guess > 100:
          print("Please enter a number between 1 and 100.")
          continue 

        #Only valid guesses count
        Guesses += 1

        if Guess < secret_number:
            print("Higher!")

        elif Guess > secret_number:
            print("Lower!")

        else:
            print("Correct!")
            break


    #Print number of guesses
    print(f"You got the number in {Guesses} guesses!")

    #Print a message based on performance
    if Guesses <= 3:
        print("Amazing!")

    elif Guesses <= 5:
        print("Woohoo!")

    elif Guesses <= 7:
        print("Not bad!")

    elif Guesses <= 9:
        print("Do you even play this game?")

    else:
        print("Go back to Middle School!")

def main():
    play_again = "Y"

    while play_again.lower() == "y":
        play_game()

        play_again = input("Do you want to play again? (Y/N): ")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()