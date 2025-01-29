import random

colorGuess1 = ""
colorGuess2 = ""
colorGuess3 = ""
colorGuess4 = ""
rounds = 9
amountSlot = 0
amountColor = 0
guessTF = True
cheat = False # True = shows the hidden pattern, False = doesn't show the hidden pattern


def Accepted(letter, guessNum):
    # finds if the letter inputted is able to be used and tell which guess was Invalid
    guessNumL = ""

    if guessNum == 1:
        guessNumL = "first guess"
    elif guessNum == 2:
        guessNumL = "second guess"
    elif guessNum == 3:
        guessNumL = "third guess"
    elif guessNum == 4:
        guessNumL = "first fourth"

    while not ((letter == "r") or (letter == "b") or (letter == "g") or (letter == "y") or (letter == "o") or (letter == "p")):
        letter = input("Invalid letter for " + guessNumL + ", try again: ")

    return letter


def Guessing():
    # gets a input for the guess and makes it a variable
    global colorGuess1, colorGuess2, colorGuess3, colorGuess4
    colorGuess1 = input("What's your first guess: ")
    colorGuess1 = Accepted(colorGuess1, 1)
    colorGuess2 = input("What's your second guess: ")
    colorGuess2 = Accepted(colorGuess2, 2)
    colorGuess3 = input("What's your third guess: ")
    colorGuess3 = Accepted(colorGuess3, 3)
    colorGuess4 = input("What's your fourth guess: ")
    colorGuess4 = Accepted(colorGuess4, 4)
    print("")


def randLetter():
    global randNum
    randInt = random.randint(1, 6)
    randStr = ""
    randNum.append(randInt)

    # print(randNum)
    # print(randInt in randNum)

    if randInt in randNum:
        if randInt == 1:
            randStr = "r"
        elif randInt == 2:
            randStr = "b"
        elif randInt == 3:
            randStr = "g"
        elif randInt == 4:
            randStr = "y"
        elif randInt == 5:
            randStr = "o"
        elif randInt == 6:
            randStr = "p"

    return randStr


def Confirm():
    global guessTF

    while True:
        PrintGuess()
        confirming = input("Is this your guess? y or n: ")

        if confirming == "n":
            Guessing()
        elif confirming == "y":
            guessTF = False
            break
        else:
            print("Invalid letter, try again\n")


def DetermineMatch(patternSlot1, patternSlot2, patternSlot3, patternSlot4):
    global amountSlot, amountColor
    amountSlot = 0

    for i in range(4):
        if i == 0:
            if colorGuess1 == patternSlot1:
                amountSlot += 1
            elif colorGuess1 == patternSlot1 or colorGuess1 == patternSlot2 or colorGuess1 == patternSlot3 or colorGuess1 == patternSlot4:
                amountColor += 1

        elif i == 1:
            if colorGuess2 == patternSlot2:
                amountSlot += 1
            elif colorGuess2 == patternSlot1 or colorGuess2 == patternSlot2 or colorGuess2 == patternSlot3 or colorGuess2 == patternSlot4:
                amountColor += 1

        elif i == 2:
            if colorGuess3 == patternSlot3:
                amountSlot += 1
            elif colorGuess3 == patternSlot1 or colorGuess3 == patternSlot2 or colorGuess3 == patternSlot3 or colorGuess3 == patternSlot4:
                amountColor += 1

        elif i == 3:
            if colorGuess4 == patternSlot4:
                amountSlot += 1
            elif colorGuess4 == patternSlot1 or colorGuess4 == patternSlot2 or colorGuess4 == patternSlot3 or colorGuess4 == patternSlot4:
                amountColor += 1


def endRound():
    global rounds, guessTF, amountSlot, amountColor

    if amountSlot == 4 or rounds == 0:
        if amountSlot == 4:
            print("\nYou guessed the correct pattern!")
            roundsTook = 10 - rounds

            if roundsTook == 1:
                print("It took " + str(roundsTook) + " guess to get it right")
            elif roundsTook == 0:
                print("It took you all 10 rounds to guess it right")
            else:
                print("It took " + str(roundsTook) + " guess to get it right")

        else:
            print("\nSorry but you're out of rounds to guess, the pattern was " + RL1 + " " + RL2 + " " + RL3 + " " + RL4)

        rounds = -1
    else:
        print("\nYou got " + str(amountSlot) + " slots correct\nYou got " + str(amountColor) + " colors correct")

        if rounds == 1:
            print("There is " + str(rounds) + " round left!\n")
        else:
            print("There are " + str(rounds) + " rounds left\n")

        print("Colors: Red=r Blue=b Green=g Yellow=y Orange = o Purple=p\n")

        guessTF = True
        rounds -= 1
        amountColor = 0


def PrintGuess():
    print(colorGuess1 + " " + colorGuess2 + " " + colorGuess3 + " " + colorGuess4)


print("\nGuess colors to find the correct pattern \nColors: Red=r Blue=b Green=g Yellow=y Orange = o Purple=p\n")

# makes a random hidden pattern
randNum = []
RL1 = randLetter()
RL2 = randLetter()
RL3 = randLetter()
RL4 = randLetter()
# to see what the random letters give
if cheat:
    print(RL1 + "" + RL2 + "" + RL3 + "" + RL4)
# sets a hidden pattern for testing
# RL1 = "g"
# RL2 = "b"
# RL3 = "y"
# RL4 = "p"

# tells the user what easy and hard mode dose and asks for a mode


while rounds != -1:
    # asks the user for four inputs as a guess
    Guessing()

    # shows the user their guess and asks to confirm if right, if wrong they can reenter their guess
    while guessTF:
        Confirm()

    # determine if the users guess matches the hidden pattern
    DetermineMatch(RL1, RL2, RL3, RL4)

    # ends the round and starts new one unless pattern was guessed correctly or the rounds run out
    endRound()
