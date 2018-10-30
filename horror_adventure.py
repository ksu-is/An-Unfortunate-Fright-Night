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
    print("You hear the sound of a piano coming from the house.")
    time.sleep(3)
    print('Do you go inside or go to the party?')
    time.sleep(3)
    print('...')

def chooseOption():
    option = ""
    while option != "H" and option != "P": #input validation
        option = input("Choose a path: (H or P): " )

    return option

def checkOption(chosenOption):
    print("You have made a decision.")
    time.sleep(2)
    print("There's a creepy clown standing at the stop sign near you.")
    time.sleep(2)
    print("The clown starts heading in your direction, laughing.")
    time.sleep(2)

    chosenOption == ""
    option = ""

    if option == "":
        print("The clown was just a figment of your imagination.")
        time.sleep(3)
        print("Your friend pulls up and asks if you want a lift to the party.")
        print("You have chosen wisely.  You are safe...for now...")

    while
        option == "":
            print("A burst of cold air brushes your shoulder and the door to the house slams shut.")
            time.sleep(3)
            print("A masked man comes out of the kitchen with an electric chainsaw.")
            time.sleep(3)
            print("He walks towards you, reving the saw.")
            time.sleep(3)
            print("You stumble as you flee to escape.")
            time.sleep(3)
            print("The masked man stands over your body and ends your existance.")
    elif
        option == "":   
            print("You run away from the clown, terrified for your life.")
            print("You accidently trip and fall, but when you try to get up, you are greeted by the terrifying grin of the creepy clown.")
            print("You open your mouth to scream for help, but it is too late!")
            print("The clown puts you in a bag, picks you up, and walks away laughing")
            print("You are now a prisoner of the clown.")
    else
        option == "":
            print("The sound of the piano and the eeriness of the abandoned house make you want to skip the party.")
            print("You turn around, and head home.")


playAgain = "Yes"
while playAgain == "Yes" or playAgain == "Y" or playAgain == "y" or playAgain == "yes":
    displayIntro()
    choice = chooseOption()
    checkOption(choice) #choice is equal to "1" or "2"
    playAgain = input("Do you want to play again? (Yes or y to go again.) ")
    
    if playAgain == "No" or playAgain =="n":
        print("Better luck next time.  Happy Halloween! (:")
