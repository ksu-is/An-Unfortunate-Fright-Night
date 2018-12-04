# name: Shannon Jones and Sydney Elledge
# date: 2018-10-23
# description: Text-based horror adventure game

import random
import time

def displayIntro():
    print("It was a dark and spooky night.")
    time.sleep(3)
    print("You come across a haunted, abandoned house on your way to your friend's Halloween party.")
    time.sleep(3)
    print("You are curious to see what is inside.")
    time.sleep(3)
    print('Go inside or Go to the party?')
    time.sleep(3)
    print('...')

def chooseOption():
    option = ""
    while option != "1" and option != "2": #input validation
        option = input("Choose a path: (1 or 2): " )

    return option

def checkOption(chosenOption):
    print("You have made a decision.")
    time.sleep(2)
    print("There's a creepy clown standing at the stop sign near you.")
    time.sleep(2)
    print("The clown starts heading in your direction, laughing.")
    time.sleep(2)

    correctOption = random.randint(1, 2)

    if chosenOption == str(correctOption):
        print("Luckily, the clown was just a figment of your imagination.")
        time.sleep(3)
        print("Your friend pulls up and asks if you want a lift to the party.")
        print("You have chosen wisely.  You are safe...for now...")
    else:
        print("A burst of cold air brushes your shoulder and the door to the house slams shut.")
        time.sleep(3)
        print("A masked man comes out of the kitchen with an electric chainsaw.")
        time.sleep(3)
        print("He walks towards you, reving the saw.")
        time.sleep(3)
        print("You stumble as you flee to escape.")
        time.sleep(3)
        print("The masked man stands over your body and ends your existance.")


playAgain = "Yes"
while playAgain == "Yes" or playAgain == "y":
    displayIntro()
    choice = chooseOption()
    checkOption(choice) #choice is equal to "1" or "2"
    playAgain = input("Do you want to play again? (Yes or y to go again.) ")
    
    if playAgain == "No" or playAgain =="n":
        print("Better luck next time.  Happy Halloween! (:")
