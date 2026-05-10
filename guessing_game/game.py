import random

# random is a built-in Python library
# it lets us generate random numbers

def get_random_number():
    # this is a function — a reusable block of code
    # random.randint gives us a whole number between 1 and 10
    return random.randint(1, 10)

def play_game():
    secret = get_random_number()
    attempts = 0

    print("I picked a number between 1 and 10. Can you guess it?")

    while True:
        # while True means loop forever until we say stop
        guess = input("Your guess: ")

        # input() always returns a string
        # int() converts it to a number so we can compare
        attempts = attempts + 1
        if attempts >= 5:
            print("Game Over! The number was", secret)
            break
        
        try:
            guess = int(guess)
        except ValueError:
            print("That's not a number. try again")
            continue

        if guess < 1 or guess > 10:            
            print("Please guess a number between 1 and 10")
            continue
                
        if guess < secret:
            print("Too low, try again")
        elif guess > secret:
            print("Too high, try again")
        else:
            # this only runs when guess == secret
            print("Correct! You got it in", attempts, "attempts")
            break
            # break exits the while loop
play_game()