import numpy as np
import random

letters = ["WARN", "WALD", "WESPEN", "WESTEN", "HUMMEL", "BUMMEL", "FLUG", "ZUG", "NEST", "STICH", "SCHUMMEL", "TEST"]
vowels = [0, 0, 1, 1, 4, 4, 4, 4, 1, 2, 4, 1]
syllables = [1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1]
vowelNames = ["A", "E", "I", "O", "U"]

letters = ["PLAY", "RIGHT", "WIDE", "TWO", "TO", "DAYS", "IN", "SIDE", "OTHER", "KEY", "TREE", "MOON", "YOU", "SET", "SELL",
           "RIGHT", "WIDE", "HEART", "ART", "CHILD", "TRUE", "BLUE", "GREEN", "BLUE", "ONE", "LOVE", "ON", "DAY", "BRIGHT",
            "LIFE", "SCIENCE", "EYE", "MIND", "MOVIE", "MY", "SHE", "MOVES", "SHOES", "SKY", "WRIGHT", "SELF", "FALL", "DREAM", "LIGHT", "TIME"]

vowels = [4, 5, 5, 2, 4, 4, 4, 4, 1, 2, 4, 1]
syllables = [1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1]
vowelNames = ["A", "E", "I", "O", "U"]


letterAtPlace = []
positionNames = ["Schloss", "Auto", "Berge", "Fußabdruck", "Eisenbahn", "Baum", "Vögel", "Fluß", "Cafe", "Handabdruck"]
playerNames   = ["Mirabelle", "Marcelle", "Johannes", "Michelle", "Katharina", "Theodora", "Ricciardo"]
riddlesAtPlace = []
solvedLetters = dict ()
riddles = [[0, 2], [1, 2],
           [0, 3], [1, 3], 
           [0, 2, 8], [1, 2, 8], [0, 3, 8], [1, 3, 8],
           [0, 2, 9], [1, 2, 9], [0, 3, 9], [1, 3, 9],
           [0, 2, 11], [1, 2, 11], [0, 3, 11], [1, 3, 11],
           [4, 6], [5, 6],
           [4, 7], [5, 7],
           [10, 7], [10, 6]]
playerPlaces = []
playerLetters = []
playerPoints = []
playerCount = 0
edges = [
    [1, 5, 4],
    [2, 6, 0],
    [3, 7, 1],
    [4, 8, 2],
    [0, 9, 3],

    [6, 1, 9, 7, 8, 0],
    [7, 2, 5, 8, 9, 1],
    [8, 3, 6, 5, 9, 2],
    [9, 4, 7, 6, 5, 3],
    [5, 6, 8, 7, 6, 4],
]
currentPlayer = 0
gameFinished = False

def distributeLetters (_letters):
    global letterAtPlace
    letterAtPlace = _letters.copy ()
    random.shuffle (letterAtPlace)
    return letterAtPlace

def distributeRiddles (_riddles):
    for i in range (0, 10):
        riddlesAtPlace.append (-1)
    for r in _riddles:
        index = int (np.random.rand () * 10)
        while riddlesAtPlace [index] != -1:
            index = int (np.random.rand () * 10)
        riddlesAtPlace [index] = r
    return riddlesAtPlace

def distributePlayers ():
    for i in range (0, playerCount):
        index = int (np.random.rand () * 10)
        while index in playerPlaces:
           index = int (np.random.rand () * 10)
        playerPlaces.append (index) 

def printPlayers ():
    for i in range (0, len (playerPlaces)):
        printPlayer(i)

def printPlayer(i):
    p = playerPlaces[i]
    print ("Player " + str (i) + " is at place " + str(p) + " .")
    if riddlesAtPlace [p] == -1:
        print ("There is no riddle at this place. ")
    else:
        print ("There is a riddle at this place! ")
    if letterAtPlace [p] == -1:
        pass #print ("There is no letter at this place. ")
    else:
        pass #print ("There is the letter " + letters [letterAtPlace[p]] + " at this place")
    print ("----")

def newGame ():
    global playerCount
    playerCount = askPlayerCount ()
    for i in range (0, playerCount):
        playerLetters.append (-1)
        playerPoints.append (0)
    selLetters = selectLetters ()
    selRiddles = selectRiddles (selLetters)
    distributeLetters (selLetters)
    printRiddles (selRiddles)
    distributeRiddles (selRiddles)
    distributePlayers ()
    distributeLetters (selLetters)
    printPlayers ()
    while gameFinished == False:
        makeMove ()

def selectRiddles (_letters):
    selectedRiddles = []
    random.shuffle(riddles)
    for r in riddles:
        possible = True
        for x in r:
            if (x in r) == False:
                possible = False
        if possible and len (selectedRiddles) < 10:
            selectedRiddles.append (r)
    return selectedRiddles

def selectLetters ():
    selectedLetters = []
    while len (selectedLetters) < 10:
        index = 0
        while index in selectedLetters:
            index = int (np.random.rand () * len (letters))
        selectedLetters.append (index)
    print ("SELECTED LETTERS ARE " + str (selectedLetters))
    return selectedLetters

def askPlayerCount ():
    count = input ("How many players are playing? ")
    return int (count)

def createHint (riddle, position):
    _letter = riddle [position]
    _vowel = vowelNames [vowels [_letter]]
    _syllables = syllables [_letter]
    return "Das " + str (position + 1) + ". Wort hat ein " + _vowel + " und " + str (_syllables) + " Silben."



def printRiddles (_riddles):
    for r in _riddles:
        printRiddle(r)
        print ("--------")

def dropRandomHint (r):
    i = int (np.floor (np.random.rand () * len (r)))
    return createHint (r, i)

def printRiddle(r):
    concat = ""
    for x in r:
        concat += letters [x]
    print (concat)
    for i in range (0, len (r)):
        print (createHint (r, i))

        
def tryToSolve (currentPlayer, currentLetter, riddleAtPlace):
    if currentLetter in riddleAtPlace:
        print ("You have the correct letter for this riddle!")
        if str(riddleAtPlace) in solvedLetters:
            solvedLetters[str(riddleAtPlace)].append (currentLetter)
        else:
            solvedLetters[str(riddleAtPlace)] = [currentLetter]
        points = len (solvedLetters[str(riddleAtPlace)]) * 5
        print ("You receive " + str(points) + " points!")
        playerPoints [currentPlayer] += points
    else:
        print ("Unfortunately this is not the right letter!")
def makeMove ():
    global currentPlayer
    print (" ")
    print ("===///===///===///===///")
    for p in range (0, len (playerPoints)):
        pnts = playerPoints[p]
        print ("Player " + str(p) + " has " + str(pnts) + " points!")
    print ("1)")
    print ("Hello player " + playerNames [currentPlayer] + ". ")
    pos = playerPlaces [currentPlayer]
    print ("You are at position " + positionNames [pos])
    currentLetter = playerLetters [currentPlayer]
    if currentLetter != -1:
        print ("Your current letter is " +  str (letters[currentLetter]))
    else:
        print ("You do not have a letter right now!")
    options = edges [pos]
    printOptions(options)
    inputRequired = True
    while inputRequired:
        select = ""
        while select not in ["N", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            select = input ("Where do you want to go? ")
        if select == "N":
            print ("You decided to not move. ")
            printPlayer (currentPlayer)
            inputRequired = False
        else:
            select = int (select)
            if select in options:
                playerPlaces [currentPlayer] = select
                print ("Great! You went to place " + positionNames[select])
                inputRequired = False
            else:
                print ("Oops! This is not possible.")
                printOptions(options)

    print ("2)")
    p = playerPlaces[currentPlayer]
    riddleAtPlace = riddlesAtPlace[p]
    if riddleAtPlace:
        print ("There is a riddle here!")
        select = ""
        while select not in ["H", "S", "I"]:
            select = input ("Do you want a Hint (H), try to solve the riddle with your letter (S), or ignore the riddle (I)?")
        if select == "I":
            pass
        elif select == "H":
            print (dropRandomHint (riddleAtPlace))
            currentPlayer = (currentPlayer + 1) % playerCount
            return
        elif select == "S":
            tryToSolve (currentPlayer, currentLetter, riddleAtPlace)
            currentPlayer = (currentPlayer + 1) % playerCount
            return
    takeLetter = False
    inputRequired = True
    swap = False
    print ("---")
    print ("3) ")
    if playerLetters [currentPlayer] == -1:
        print ("You currently have no letter.")
    else:
        print ("You currently have letter " + str (letters[playerLetters [currentPlayer]]) + ".")
        swap = True
    if letterAtPlace [playerPlaces[currentPlayer]] == -1:
        print ("There is no letter here.")
    else:
        print ("At this place, there is the letter " + str(letters [letterAtPlace [playerPlaces[currentPlayer]]]))
    if letterAtPlace [playerPlaces[currentPlayer]] != -1 or playerLetters [currentPlayer] != -1:
        while inputRequired:
            entry = ""
            if swap == False:
                entry = ""
                while entry not in ["Y", "N"]:
                    entry = input ("Do you want to take this letter? (Y/N) ")
            else:
                entry = ""
                while entry not in ["Y", "N"]:
                    entry = input ("Do you want to swap your letter with this one? (Y/N) ")
            if entry == "Y":
                inputRequired = False
                if swap == False:
                    playerLetters [currentPlayer] = letterAtPlace [playerPlaces[currentPlayer]]
                    letterAtPlace [playerPlaces[currentPlayer]] = -1 
                else:
                    c = playerLetters [currentPlayer] 
                    playerLetters [currentPlayer] = letterAtPlace [playerPlaces[currentPlayer]]
                    letterAtPlace [playerPlaces[currentPlayer]] = c
                    print ("At place " + str(playerPlaces[currentPlayer]) + " there is now " + str(playerPlaceLetter()) + ".")
                if playerLetters [currentPlayer] == -1:
                    print ("You now have no letter.")
                else: 
                    print ("You now have the " + str(letters[playerLetters [currentPlayer]]) + " letter.")
            elif entry == "N":
                print ("Ok, you chose to not change anything.")
                inputRequired = False
            else:
                print ("Oops! That is not possible, try again.")
            
            print ("#######")


        
    #print ("Do you want to solve a riddle?")
    #print ("Do you want to drop your letter?")
    #print ("Do you want to pick up a letter?")
    currentPlayer = (currentPlayer + 1) % playerCount

def playerPlaceLetter():
    if letterAtPlace [playerPlaces[currentPlayer]] == -1:
        return "no letter." 
    return letters[letterAtPlace [playerPlaces[currentPlayer]]]

def printOptions(options):
    position_text = ""
    for option in options:
        position_text += " " + positionNames[option] + "(" + str (option) + ")"
    print ("You can go to" + position_text + " or not move with N.")

newGame ()