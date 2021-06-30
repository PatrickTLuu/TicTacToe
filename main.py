import random

grid = [
" ", " ", " ",
" ", " ", " ",
" ", " ", " "
]


# Function that prints the current grid
def PrintGrid():
    print("\n\n")
    print(" | 1 | 2 | 3 |")
    print("-|-----------|")
    print("A| " + grid[0] + " | " + grid[1] + " | " + grid[2] + " |")
    print("-|-----------|")
    print("B| " + grid[3] + " | " + grid[4] + " | " + grid[5] + " |")
    print("-|-----------|")
    print("C| " + grid[6] + " | " + grid[7] + " | " + grid[8] + " |")
    print("-|-----------|\n\n")


# Function that contains the code for any player's move
def humansMove(turn):
    validPlay = False
    letter = ""
    number = ""
    cordToInt = {"A": -1, "B": 2, "C": 5}

    # Repeats until player enters a valid coordinate
    while not validPlay:

        # Split the coordinate
        inputStr = input("Enter coordinate: ")
        letter = inputStr[0]
        number = int(inputStr[1])
            
        # Check if coordinates are valid
        if (letter in "ABC") and (number <= 3):
            index = cordToInt[letter] + number
            if grid[index] == " ":
                grid[index] = turn
                validPlay = True


# Function that contains the code for any computer move
def compMove(turn):
    validComp = False

    #Repeats until a valid coordinate is chosen
    while not validComp:
        compMove = random.randint(0, 8)
        if grid[compMove] == " ":
            grid[compMove] = turn
            validComp = True


# Checks if anyone has won
def hasWon():
    possibleWins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    # Checks for all possible win combos
    try:
        for set in possibleWins:
            if grid[set[0]] == grid[set[1]] == grid[set[2]] != " ":
                print("\n\nCongratulations "+ grid[set[0]] + " wins!")
                print("Do you want to play again (Y/N)? ")
                replay = input(">>> ") == "Y"

                if replay:
                    setup()

                else: 
                    exit()
        grid.index(" ")


    # If there are no empty spaces and no winners, ends the game
    except ValueError:
        print("\n\nStalemate!")
        print("Do you want to play again (Y/N)? ")
        replay = input(">>> ") == "Y"

        if replay:
            setup()

        else: 
            exit()


# One player game       
def OnePlayer(goesFirst):
    winner = False

    if goesFirst == "Y":
        comp = "O"
        play = "X"

        while not winner:
            PrintGrid()
            humansMove(play)     
            hasWon()

            PrintGrid()
            compMove(comp)
            hasWon()

    else:
        comp = "X"
        play = "O"

        while not winner:
            PrintGrid()
            compMove(comp)

            PrintGrid()
            hasWon()

            humansMove(play)
            hasWon()


def TwoPlayers(playOne, playTwo):
    winner = False

    while not winner:
        PrintGrid()
        hasWon()
        print(playOne + "'s Turn")
        humansMove("X")

        PrintGrid()
        hasWon()

        print("\n\n" + playTwo + "'s Turn")
        humansMove("O")


def setup():
    for i in range(9):
        grid[i] = " "

    print("Welcome to Hack It Forward Tic Tac Toe!")
    print("1 or 2 Players?")
    mode = input(">>> ")

    if "1" in mode:
        print("\nWould you like to go first (Y/N)?")
        first = input(">>> ")
        OnePlayer(first)
    
    else:
        print("\nNote: Player One will always go first")
        playOneName = input("Enter Player One's Name: ")
        playTwoName = input("Enter Player Two's Name: ")
        TwoPlayers(playOneName, playTwoName)

if __name__ == '__main__':
    setup()

    


    
