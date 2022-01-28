from utils.gamePieces import referenceTable, wins, playerOnePrompt, playerTwoPrompt, playerVictory, tableDivider
from utils.interfaceUtils import getGameGrid, getWinningGameGrid, clearScreen

table = [
    "-","-","-",
    "-","-","-",
    "-","-","-"
]
winString = ""
playerOneTurn = True
error = False
winner = False
tie = False

clearScreen()
# Game loop
while not winner:
    # Ouput instructions, reference table, and game grid
    gameTable = getGameGrid(table)
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
    if (int(playerInput) > 8):
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
    gameTable = getWinningGameGrid(table, winString)
    print(referenceTable + "\n\n" + tableDivider + "\n\n" + gameTable + "\n")
    print(playerVictory.format("one" if not playerOneTurn else "two"))

# If there is a tie, displaye the final grid and declare the tie
if tie:
    gameTable = getGameGrid(table)
    print(referenceTable + "\n\n" + tableDivider + "\n\n" + gameTable + "\n")
    print("It's a tie!")

# Stop the program from ending automatically
input("Press \"Enter\" to end.")
clearScreen()