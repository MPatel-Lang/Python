# Mehul Patel
#Date: 10/3/2021
#Game of Rock, Paper, Scissors
#Choose Rock, Paper, Scissors. It is case sensitive and numbers will not work.

from random import randint

#A list of options
Input = ["Rock", "Paper", "Scissors"]

#Assigns a random play to the computer
Computer = Input[randint(0,2)]

#Sets player as True
Player = True

while Player == True:
#Sets player to False
    Player = input("Rock, Paper, Scissors?")
    if Player == Computer: #Tie
        print("Tie!")
    elif Player == "Scissors": #Player: Scissors
        if Computer == "Rock":  #Computer: Rock
            print("You lose...", Computer, "destroys", Player)
        else:
            print("You win!", Player, "cut", Computer)
    elif Player == "Paper":  #Player: Paper
        if Computer == "Scissors":  #Computer: Scissors
            print("You lose!", Computer, "cut", Player)
        else:
            print("You win!", Player, "covers", Computer)
    
    elif Player == "Rock":  #Player: Rock
        if Computer == "Paper":   #Computer: Paper
            print("You lose!", Computer, "covers", Player)
        else:
            print("You win!", Player, "destroys", Computer)
    else:
        print("That is invalid input. Please check your input! Spelling, Lowercase and Numbers are common problems.")
    #player was set to False, but we want it to be True so the loop continues
    Player = True

    #Assigns a random play to the computer
    Computer = Input[randint(0,2)]
