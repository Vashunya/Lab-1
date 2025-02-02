import random

def guess_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20. Take a guess.")
    num_to_guess = random.randint(1, 20)
    count = 1
    while True:
        number = int(input("Take a guess: "))
        if num_to_guess == number:
            print(f"Good job, {name}! You guessed my number in {count} guesses!")
            break
        elif number > num_to_guess:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
        count+=1


guess_number()