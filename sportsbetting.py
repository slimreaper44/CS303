blah = (1, 7, 19, 22, 24, 8)

for number in blah:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")










# from random import randint


# print("Welcome to the Higher or Lower game!")

# solution = randint(1, 100)  # Random answer
# num_guesses = 0
# guess = 0

# # Keep guessing until correct
# while guess != solution:
#     guess = int(input("Guess a number between 1 and 100: "))

#     # Validate range
#     while guess < 1 or guess > 100:
#         guess = int(input("Invalid number. Try again: "))

#     num_guesses += 1  # Count valid guesses

#     if guess > solution:
#         print("Lower")
#     elif guess < solution:
#         print("Higher")
#     else:
#         print("You guessed it!")

# print(f"It took you {num_guesses} guesses to find the number {solution}.")