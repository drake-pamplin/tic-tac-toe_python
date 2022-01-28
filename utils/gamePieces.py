referenceTable =(
    "Enter a number in the table below to place your mark:\n\n"
    " 0 | 1 | 2" + "\n" +
    "───────────\n" +
    " 3 | 4 | 5" + "\n" +
    "───────────\n" +
    " 6 | 7 | 8"
)

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

tableDivider = "====================================================="

playerOneText = "\033[1;31;47m"
playerTwoText = "\033[1;34;47m"
winTextStart = "\033[0;37;42m"
normalTextStart = "\033[0m"

playerVictory = "Congratulations player {}!"

playerOnePrompt = "P1 input: "
playerTwoPrompt = "P2 input: "