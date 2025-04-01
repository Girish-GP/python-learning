'''
snake > water
water > gun
gun > snake

for snake = 1
for water = 0
for gun = -1     
'''

import random;

computerList = [1,0,-1]
selectionDict = {
    1:"Snake",
    0:"Water",
    -1:"Gun" 
}

def playGame():
    random_number = random.randint(0,2)
    computerSelection = computerList[random_number]
    userSelection = int(input("Enter your choice:"))
    if computerList.index(userSelection) != ValueError:
        checkWinner(computerSelection,userSelection)
        confirmation()
    else:
        print("Invalid choice")
        confirmation()

def checkWinner(computerSelection,userSelection):
    print(f"Your choice is {selectionDict[userSelection]}")
    print(f"Computer choice is {selectionDict[computerSelection]}")
    if computerSelection == userSelection:
        print("Game Draw")
        confirmation()
    else: #1 > 0 , 0 > -1 , -1 > 1
        if computerSelection == 1 and userSelection == -1:
            print("User win")
        elif computerSelection == 1 and userSelection == 0:
            print("Computer win")
        elif computerSelection == 0 and userSelection == 1:
            print("User win")
        elif computerSelection == 0 and userSelection == -1:
            print("Computer win")
        elif computerSelection == -1 and userSelection == 1:
            print("Computer win")
        elif computerSelection == -1 and userSelection == 0:
            print("User win")
        
    print("Game Over")

def confirmation():
    choice = input("Do you want to play again ? y or n:")
    if choice == 'y':
        playGame()
    
playGame()