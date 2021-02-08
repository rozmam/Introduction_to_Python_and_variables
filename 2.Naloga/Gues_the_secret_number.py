secret = 42

guess = int(input("Guess the secret number (Between 1 and 50): "))

if guess == secret:
    print("Congratulations for guessing the right number!")
else:
    print("Your guess is wrong!")