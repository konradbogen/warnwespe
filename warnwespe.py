import numpy as np
import random

letters = ["WARN", "WALD", "WESPEN", "WESTEN", "HUMMEL", "BUMMEL", "FLUG", "ZUG", "NEST", "STICH", "SCHUMMEL", "TEST"]
vowels = [0, 0, 1, 1, 4, 4, 4, 4, 1, 2, 4, 1]
syllables = [1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1]
vowelNames = ["A", "E", "I", "O", "U"]
letterAtPlace = []
riddlesAtPlace = []
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
        p = playerPlaces[i]
        print ("Player " + str (i) + " is at place " + str(p) + " .")
        if riddlesAtPlace [p] == -1:
            print ("There is no riddle at this place. ")
        else:
            print ("There is the following riddle at this place: ")
            printRiddle (riddlesAtPlace [p])
        if letterAtPlace [p] == -1:
            print ("There is no letter at this place. ")
        else:
            print ("There is the letter " + letters [letterAtPlace[p]] + " at this place")
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

def printRiddle(r):
    concat = ""
    for x in r:
        concat += letters [x]
    print (concat)
    for i in range (0, len (r)):
        print (createHint (r, i))

def makeMove ():
    print ("Do you want to stay or move?")
    print ("Do you want to solve a riddle?")
    print ("Do you want to drop your letter?")
    print ("Do you want to pick up a letter?")

newGame ()