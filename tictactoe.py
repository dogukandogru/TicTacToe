# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:58:38 2020

@author: Dogukan Dogru
"""



def printTable(table):
    print()
    print("   1 2 3")
    for i in range(3):
        print(str(i+1) + " ", end = " "),
        for k in range(3):
            print(table[i][k], end = " "),
        print("")
    print()



def playX(table,move1,move2):
    table[move1][move2] = "X"   
    
def playO(table,move1,move2):
    table[move1][move2] = "O" 
    
    
def checkRows(table):
    constX = "['X', 'X', 'X']"
    constO = "['O', 'O', 'O']"
    if str(table[0]) == constX or str(table[1]) == constX or str(table[2]) == constX:
        return "X"
    elif str(table[0]) == constO or str(table[1]) == constO or str(table[2]) == constO:
        return "O"


def checkColumns(table):
   column1 = table[0][0] + table[1][0] + table[2][0]
   column2 = table[0][1] + table[1][1] + table[1][1]
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

table = [["-", "-", "-"],["-", "-", "-"],["-", "-", "-"]] 

print("Welcome to TicTacToe. Choose the game mode")
print("1- Player vs Computer")
print("2- Player vs Player")

gameMode = input()
printTable(table)
if gameMode == "1":
    print("")
elif gameMode == "2":
    for i in range(0,9):
        if i%2 == 0:
            print("1. Player's Move:", end = " "),
            move = input()
            move1 = int(move[0])-1
            move2 = int(move[2])-1
            playX(table,move1,move2) 
              
            
        if i%2 == 1 :
            print("2. Player's Move:", end = " "),
            move = input()
            move1 = int(move[0])-1
            move2 = int(move[2])-1
            playO(table,move1,move2)
    
                
        printTable(table)
        if checkTable(table) != "":
            print(checkTable(table))
            break



print("Game Over")





















