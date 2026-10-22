import random
# Pick a secret word
def choose_word():
    words = ["plant", "crane", "slate", "brick", "flame"]   
    return random.choice(words)

# get and validate the user's guess
def get_guess(previous_guesses):
    guess = input("Enter a five letter word: ").lower()


    while len(guess) != 5 or not guess.isalpha() or guess in previous_guesses:
        if len(guess) != 5:
            print("Please enter exactly a five letter word.")
        elif not guess.isalpha():
            print("Please enter only letters.")
        elif guess in previous_guesses:
            print("You have already guessed that word. Try again.")
        guess = input("Enter a five letter word: ").lower()

    return guess

# Compare the guess to the secret word
def evaluate_guess(guess, secret_word):
    feedback = []
    for i in range(5):
        if guess[i] == secret_word[i]:
            feedback.append("G")
        elif guess[i] in secret_word:
            feedback.append("Y")
        else:
            feedback.append("B")
    return feedback

# Show guess and give comments
def Display_guess(guess, feedback):
    print("Guess:", " ".join(guess.upper()))
    print("Feedback:", " ".join(feedback))

# Did the guy win
def has_won(guess, secret_word):
    return guess == secret_word