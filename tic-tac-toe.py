import os
from platform import system as systemName

referenceTable =(
    "Enter a number in the table below to place your mark:\n\n"
    " 0 | 1 | 2" + "\n" +
    "───────────\n" +
    " 3 | 4 | 5" + "\n" +
    "───────────\n" +
    " 6 | 7 | 8"
)
table = [
    "-","-","-",
    "-","-","-",
    "-","-","-"
]
wins = [
    "012",
    "345",
    "678",
    "036",
    "147",
    "258",
    "048",
    "246"
]
winString = ""
playerOnePrompt = "P1 input: "
playerTwoPrompt = "P2 input: "
playerVictory = "Congratulations player {}!"
tableDivider = "====================================================="
greenTextStart = "\033[92m"
normalTextStart = "\033[0m"
playerOneTurn = True
error = False
winner = False
tie = False

# Returns game grid
def getGameGrid():
    output = ""
    counter = 0
    for spot in table:
        output += (" " + spot + " ")
        if counter % 3 == 2 and counter < 8:
            output += "\n───────────\n"
        elif counter < 8:
            output += "|"
        counter += 1
    return output

def getWinningGameGrid(win):
    output = ""
    counter = 0
    for spot in table:
        newSpot = ""
        if (str(counter) == win[0] or
                str(counter) == win[1] or
                str(counter) == win[2]):
            newSpot = " " + greenTextStart + spot + normalTextStart + " "
        else:
            newSpot = (" " + spot + " ")

        output += newSpot
        if counter % 3 == 2 and counter < 8:
            output += "\n───────────\n"
        elif counter < 8:
            output += "|"
        counter += 1
    return output

def clearScreen():
    command = "clear"
    if (systemName().lower() == 'windows'):
        command = "cls"
    os.system(command)

clearScreen()
# Game loop
while not winner:
    # Ouput instructions, reference table, and game grid
    gameTable = getGameGrid()
    if "-" not in gameTable:
        tie = True
        break
    print("Type \"end\" to quit.\n" + referenceTable + "\n\n" + tableDivider + "\n\n" + gameTable + "\n")
    
    # If the previous loop resulted in an error, inform the player
    if error:
        print("Bad input detected. Try again, please.")
        error = False
    
    # Ask for the proper player input (player one or player two)
    playerInput = input(playerOnePrompt if playerOneTurn else playerTwoPrompt)
        
    # Parse player input for errors
    if playerInput == "end":
        clearScreen()
        break
    try:
        int(playerInput)
    except ValueError:
        error = True
        clearScreen()
        continue
    if table[int(playerInput)] != "-":
        error = True
        clearScreen()
        continue
        
    # Insert player mark into grid
    table[int(playerInput)] = "X" if playerOneTurn else "O"
    
    # Check for winner
    spots = ""
    counter = 0
    playerToken = "X" if playerOneTurn else "O"
    for spot in table:
        if spot == playerToken:
            spots += str(counter)
        counter += 1
    for win in wins:
        if (win[0] in spots and 
                win[1] in spots and 
                win[2] in spots):
            winner = True
            winString = win
            break
    playerOneTurn = not playerOneTurn
    clearScreen()

# If there is a winner, display the final grid and results
if winner:
    gameTable = getWinningGameGrid(winString)
    print(referenceTable + "\n\n" + tableDivider + "\n\n" + gameTable + "\n")
    print(playerVictory.format("one" if not playerOneTurn else "two"))

# If there is a tie, displaye the final grid and declare the tie
if tie:
    gameTable = getGameGrid()
    print(referenceTable + "\n\n" + tableDivider + "\n\n" + gameTable + "\n")
    print("It's a tie!")

# Stop the program from ending automatically
input("Press \"Enter\" to end.")
clearScreen()