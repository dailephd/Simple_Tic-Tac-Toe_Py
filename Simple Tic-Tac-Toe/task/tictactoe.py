
def printState(s):
    chrlist = []
    # split into list of characters
    for i in s:
        chrlist.append(i)
    # turn list into a matrix 3x3
    r1 = [chrlist[i] for i in range(0, 3)]
    r2 = [chrlist[i] for i in range(3, 6)]
    r3 = [chrlist[i] for i in range(6, 9)]
    b = [r1, r2, r3]
    print("---------")
    print("|" + " " + b[0][0] + " " + b[0][1] + " " + b[0][2] + " " + "|")
    print("|" + " " + b[1][0] + " " + b[1][1] + " " + b[1][2] + " " + "|")
    print("|" + " " + b[2][0] + " " + b[2][1] + " " + b[2][2] + " " + "|")
    print("---------")
    return b


def checkWinner(b, symbol):

    if b[0][0] == b[0][1] == b[0][2] == symbol:
        return True
    elif b[1][0] == b[1][1] == b[1][2] == symbol:
        return True
    elif b[2][0] == b[2][1] == b[2][2] == symbol:
        return True
    elif b[0][0] == b[1][0] == b[2][0] == symbol:
        return True
    elif b[0][1] == b[1][1] == b[2][1] == symbol:
        return True
    elif b[0][2] == b[1][2] == b[2][2] == symbol:
        return True
    elif b[0][0] == b[1][1] == b[2][2] == symbol:
        return True
    elif b[0][2] == b[1][1] == b[2][0] == symbol:
        return True
    else:
        return False


def checkFull(s):
    if "_" in s:
        return False
    else:
        return True


def checkGameState(b, s):
    if checkWinner(b, "X") and checkWinner(b, "O"):
        print("Impossible")
        return True
    elif abs(s.count("X") - s.count("O")) >= 2:
        print("Impossible")
        return True
    elif checkWinner(b, "X") and not checkWinner(b, "O"):
        print("X wins")
        return True
    elif checkWinner(b, "O") and not checkWinner(b, "X"):
        print("O wins")
        return True
    elif checkFull(s) and not checkWinner(b, "O") and not checkWinner(b, "X"):
        print("Draw")
        return True
    elif not checkWinner(b, "X") and not checkWinner(b, "O") and not checkFull(s):
        #print("Game not finished")
        return False


def askInput():
    # Convert 2d matrix input into 1d index
    check = False
    while not check:
        move = input().split(" ")
        if not move[0].isdigit() or not move[1].isdigit():
            check = False
            print("You should enter numbers!")
        elif int(move[0]) > 3 or int(move[1]) > 3:
            check = False
            print("Coordinates should be from 1 to 3!")
        elif b[int(move[0])-1][int(move[1])-1] != "_":
            check = False
            print("This cell is occupied! Choose another one!")
        else:
            check = True
    idx = (int(move[0]) - 1) * 3 + (int(move[1]) - 1)
    return idx


def updateState(s, idx, currP):
    s = list(s)
    s[idx] = currP
    s = ''.join(s)
    return s


if __name__ == "__main__":
   s = "_________"
   currP, nextP = "X", "O"
   temp = None
   checkEnd = False
   b = printState(s)
   while checkEnd == False:
       move = askInput()
       s = updateState(s, move, currP)
       b = printState(s)
       checkEnd = checkGameState(b, s)
       # Swap currP and nextP
       temp = currP
       currP = nextP
       nextP = temp





