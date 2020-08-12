# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:58:38 2020

@author: Dogukan Dogru
"""



def printTable(table):
    for i in range(3):
        for k in range(3):
            print(table[i][k], end = " "),
        print("")




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
   column1 = table[0][0] + table[0][1] + table[0][2]
   column2 = table[1][0] + table[1][1] + table[1][2]
   column3 = table[2][0] + table[2][1] + table[2][2]
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
        return "Draw"

table = [["-", "-", "-"],["-", "-", "-"],["-", "-", "-"]] 

playO(table,0,0)
playO(table,1,1)
playO(table,2,2)

print(checkTable(table))
printTable(table)