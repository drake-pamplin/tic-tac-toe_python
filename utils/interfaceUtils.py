import os
from platform import system as systemName
from .gamePieces import greenTextStart, normalTextStart

# Returns game grid
def getGameGrid(table):
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

def getWinningGameGrid(table, win):
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