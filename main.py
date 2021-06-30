import random

grid = [
" ", " ", " ",
" ", " ", " ",
" ", " ", " "
]


def PrintGrid():
    print("\n\n")
    print(" | 1 | 2 | 3 |")
    print("-|-----------|")
    print("A| " + grid[0] + " | " + grid[1] + " | " + grid[2] + " |")
    print("-|-----------|")
    print("B| " + grid[3] + " | " + grid[4] + " | " + grid[5] + " |")
    print("-|-----------|")
    print("C| " + grid[6] + " | " + grid[7] + " | " + grid[8] + " |")
    print("-|-----------|")


def humansMove(turn):
    validPlay = False
    playMove = []
    index = ""
    while not validPlay:
        for char in input("Enter coordinate: "):
            playMove.append(char)
            
        
        if "A" == playMove[0]:
            index = int(playMove[1]) - 1
            if grid[index] == " ":
                grid[index] = turn
                validPlay == True

        elif "B" == playMove[0]:
            index = int(playMove[1]) + 2
            if grid[index] == " ":
                grid[index] = turn
                validPlay == True

        elif "C" in playMove[0]:
            index = int(playMove[1]) + 5
            if grid[index] == " ":
                grid[index] = turn
                validPlay == True


def hasWon():
    possibleWins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    try:
        grid.index(" ")
        for set in possibleWins:
            if grid[set[0]] == grid[set[1]] == grid[set[2]] != " ":
                print("Congratulations "+ grid[set[0]] + " wins!")
                print("Do you want to play again (Y/N)? ")
                replay = input(">>> ") == "Y"

                if replay:
                    setup()

                else: 
                    exit()

    except ValueError:
        print("Stalemate!")
        print("Do you want to play again (Y/N)? ")
        replay = input(">>> ") == "Y"

        if replay:
            setup()

        else: 
            exit()



        
def OnePlayer(goesFirst):
    winner = False

    if goesFirst == "Y":
        turn = "X"

        while not winner:
            PrintGrid()
            validComp = False
            humansMove(turn)
            hasWon()

            while not validComp:
                compMove = random.randint(0, 8)
                if grid[compMove] == " ":
                    grid[compMove] = "O"
                    validComp = True
    
            hasWon()

    else:
        turn = "O"

        while not winner:
            PrintGrid()
            validComp = False

            while not validComp:
                compMove = random.randint(0, 8)
                if grid[compMove] == " ":
                    grid[compMove] = "X"
                    validComp = True

            PrintGrid()
            hasWon()

            humansMove(turn)
            hasWon()


def TwoPlayers(playOne, playTwo):
    winner = False

    while not winner:
        PrintGrid()
        print(playOne + "'s Turn")
        humansMove("X")

        PrintGrid()
        hasWon()

        print("\n\n" + playTwo + "'s Turn")
        humansMove("O")
        hasWon()


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
        playOneName = input("\nEnter Player One's Name: ")
        playTwoName = input("Enter Player Two's Name: ")
        TwoPlayers(playOneName, playTwoName)

if __name__ == '__main__':
    setup()

    


    
