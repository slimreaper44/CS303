from wordle_functions import choose_word, get_guess, evaluate_guess, Display_guess, has_won

print("Welcome to Wordle!")
print("Guess the secret five letter word. You have six tries.")
print("G = Correct letter in the correct position")
print("Y = Correct letter but wrong position")
print("- = Letter isn't in the word")

play_again = "Yes"

while play_again == "Yes":

    secret_word = choose_word()
    previous_guesses = []
    won = False
    attempt = 1

    # Give the player six tries to guess the word
    while attempt <= 6 and won == False:
        print()
        print(f"Attempt {attempt} of 6")

        guess = get_guess(previous_guesses)
        previous_guesses.append(guess)

        feedback = evaluate_guess(guess, secret_word)
        Display_guess(guess, feedback)

        if has_won(guess, secret_word):
            print("Congratulations! You've guessed the word!")
            won = True
        else:
            attempt += 1


    if won == False:
        print(f"The secret word was: {secret_word.upper()}.")

    play_again = input("Do you want to play again? ").lower()

print("Thanks for playing Wordle!")