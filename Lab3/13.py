import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    attempts = 0
    
    while True:
        print("Take a guess.")
        guess = int(input())
        attempts += 1
        
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break

guess_the_number()