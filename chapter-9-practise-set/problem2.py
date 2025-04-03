# The game() function in a program lets user play a game and return the score as an integer. You need to read a file "Hi-score.txt" which will be either blank or have previous high score. You need to write the program which will update the high score when ever user breaks the previous high

import random

def game():
    userEnteredNumber = int(input("Enter a number between 1 and 100: "))
    if userEnteredNumber >= 1 and userEnteredNumber <= 100:
        random_num = random.randint(1, 100)
        if random_num < userEnteredNumber:
            return userEnteredNumber  # The score is the user's number if they pass the game
        else:
            print("User failed the game, random number was:", random_num)
            return 0  # Returning 0 if the user fails
    else:
        print("Invalid number")
        return 0  # Return 0 for invalid input

def check_high_score(score):
    try:
        with open("High-score.txt", "r") as f:
            current_high_score = f.read().strip()  # Strip to remove any surrounding whitespaces or newlines
            if current_high_score == "":  # If the file is empty, no high score is set yet
                current_high_score = 0
            else:
                current_high_score = int(current_high_score)
    except FileNotFoundError:
        current_high_score = 0  # If file doesn't exist, start from 0

    if score > current_high_score:
        with open("High-score.txt", "w") as f:
            f.write(str(score))  # Write the new high score

# Main game logic
score = game()
check_high_score(score)
