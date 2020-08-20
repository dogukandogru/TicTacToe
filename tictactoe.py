# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:58:38 2020

@author: Dogukan Dogru
"""


def printTable(table):
    print()
    print("   1 2 3")
    for i in range(3):
        print(str(i+1) + " ", end=" "),
        for k in range(3):
            print(table[i][k], end=" "),
        print("")
    print()


def isMoveValid(table, move1, move2):
    if table[move1][move2] == "-":
        return True
    else:
        return False


def playX(table, move1, move2):
    if isMoveValid(table, move1, move2) == True:
        table[move1][move2] = "X"
        return True
    else:
        return False


def playO(table, move1, move2):
    if isMoveValid(table, move1, move2) == True:
        table[move1][move2] = "O"
        return True
    else:
        return False


def playBestMove(table):
    bestScore = -99
    move1 = -1
    move2 = -1

    for i in range(0, 3):
        for j in range(0, 3):
            # is the spot available?
            if str(table[i][j]) == "-":
                table[i][j] = "X"
                score = minimax(table, 0, False)
                # print(str(i+1) + " " + str(j+1) + " " + str(score))#positions and their points
                table[i][j] = "-"
                if score > bestScore:
                    bestScore = score
                    move1 = i
                    move2 = j

    playX(table, move1, move2)


def minimax(table, depth, isMaximizing):
    if checkTable(table) != "":
        if "X" in str(checkTable(table)):
            return 1
        elif "O" in str(checkTable(table)):
            return -1
        else:
            return 0

    if isMaximizing == True:
        bestScore = -99
        for i in range(0, 3):
            for j in range(0, 3):
                # is the spot available ?
                if str(table[i][j]) == "-":
                    table[i][j] = "X"
                    score = minimax(table, depth+1, False)

                    table[i][j] = "-"
                    bestScore = max(score, bestScore)
        return bestScore

    else:
        bestScore = 99
        for i in range(0, 3):
            for j in range(0, 3):
               # is the spot available ?
                if str(table[i][j]) == "-":
                    table[i][j] = "O"
                    score = minimax(table, depth+1, True)
                    table[i][j] = "-"
                    bestScore = min(score, bestScore)
        return bestScore


def checkRows(table):
    constX = "['X', 'X', 'X']"
    constO = "['O', 'O', 'O']"
    if str(table[0]) == constX or str(table[1]) == constX or str(table[2]) == constX:
        return "X"
    elif str(table[0]) == constO or str(table[1]) == constO or str(table[2]) == constO:
        return "O"


def checkColumns(table):
    column1 = table[0][0] + table[1][0] + table[2][0]
    column2 = table[0][1] + table[1][1] + table[2][1]
    column3 = table[0][2] + table[1][2] + table[2][2]
    constX = "XXX"
    constO = "OOO"
    if column1 == constX or column2 == constX or column3 == constX:
        return "X"

    elif column1 == constO or column2 == constO or column3 == constO:
        return "O"


def checkDiagonals(table):
    diagonal1 = table[0][0] + table[1][1] + table[2][2]
    diagonal2 = table[2][0] + table[1][1] + table[0][2]
    constX = "XXX"
    constO = "OOO"
    if diagonal1 == constX or diagonal2 == constX:
        return "X"

    elif diagonal1 == constO or diagonal2 == constO:
        return "O"


def checkTable(table):
    result1 = str(checkRows(table))
    result2 = str(checkColumns(table))
    result3 = str(checkDiagonals(table))

    if result1 == "X" or result1 == "O":
        return "Winner is " + result1
    elif result2 == "X" or result2 == "O":
        return "Winner is " + result2
    elif result3 == "X" or result3 == "O":
        return "Winner is " + result3
    else:
        return ""


table = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

print("Welcome to TicTacToe. Choose the game mode")
print("1- Player vs Computer")
print("2- Player vs Player")

gameMode = input()
if gameMode == "1":
    i = 0
    while i < 9:
        if i % 2 == 0:
            print("Computer's Move")
            playBestMove(table)
        elif i % 2 == 1:
            print("Your Move : ", end=" "),
            move = input()
            move1 = int(move[0])-1
            move2 = int(move[2])-1
            playO(table, move1, move2)

        i = i+1
        printTable(table)
        print("*******************************")
        if checkTable(table) != "":
            print(checkTable(table))
            break

elif gameMode == "2":
    printTable(table)
    i = 0
    print("*******************************")
    while i < 9:
        if i % 2 == 0:
            print("1. Player's Move:", end=" "),
            move = input()
            move1 = int(move[0])-1
            move2 = int(move[2])-1
            if playX(table, move1, move2) == False:
                print("Move is invalid.")
                i = i-1

        elif i % 2 == 1:
            print("2. Player's Move:", end=" "),
            move = input()
            move1 = int(move[0])-1
            move2 = int(move[2])-1
            if playO(table, move1, move2) == False:
                print("Move is invalid.")
                i = i-1
        i = i+1
        printTable(table)
        print("*******************************")
        if checkTable(table) != "":
            print(checkTable(table))
            break


print("Game Over")
