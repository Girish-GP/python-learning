import random

random_number = random.randint(1,100)
print(random_number)
def guess_number():
    number_guessed = False
    number_of_guesses = 1
    while not number_guessed:
        user_input = int(input("Guess the number between 1 and 100:"))
        if user_input == random_number:
            number_guessed = True
            print(f"Game Over Number of guesses: {number_of_guesses}")
        if user_input > random_number:
            print(f"Number is smaller than {user_input}")
        elif user_input < random_number:
            print(f"Number is greater than {user_input}")
        number_of_guesses += 1

guess_number()
    
    
