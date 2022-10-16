from lib2to3.pgen2.token import GREATER
import os
from random import randrange
import re
from traceback import print_tb
import numpy as np


grid = []
words = []
foundedwords = []

def detectHorizontal(grid, x, y):


    for word in words:
        
        if("".join(grid[y][x: (x + len(word))]) == word):
            print("found1: " + "".join(grid[y][x: (x + len(word))]) + " " + word)
            foundedwords.append(word)
            for i in range(x, (x + len(word))):
                #grid[y][i] = '_'
                grid[y][i] = grid[y][i] + '*'
        
        #print("".join(grid[y][x - len(word) + 1: x +1]))
        # print("print: " + word[::-1] + " " +  "".join(grid[y][x - len(word) + 1: x +1]) + ".")
        # print("true: " + str(word[::-1] == "".join(grid[y][x - len(word) + 1: x +1])) )
        if("".join(grid[y][x - len(word) + 1: x +1]) == str(word[::-1])):
            print("found2: " + "".join(grid[y][x - len(word) + 1: x +1]) + " " + word[::-1]) 
            foundedwords.append(word)
            for i in range(x - len(word) + 1, x +1):
                # grid[y][i] = '_'
                grid[y][i] = grid[y][i] + '*'


def detectVertical(grid,x,y):

    for word in words:
    
        #go down
        gridword = ""

        for j in range(y, y + len(word)):
            if(j >= len(grid) or j < 0 ):
                gridword = "outofindex"
                break
            if(j < len(grid) and j >= 0 ):
                gridword += grid[j][x]

        #print(gridword)

        if(gridword == word):
            for j in range(y, y + len(word)):
                # grid[j][x] = '_'
                grid[j][x] = grid[j][x] + '*'
            foundedwords.append(word)   


        #go up
        gridword = ""

        for j in range(y - len(word) + 1, y + 1 ):
            if(j >= len(grid) or j < 0 ):
                gridword = "outofindex"
                break
            if(j < len(grid) and j >= 0 ):
                gridword += grid[j][x]

        #print(gridword)

        if(gridword == word[::-1]):
            for j in range(y - len(word) + 1, y + 1 ):
                # grid[j][x] = '_'
                grid[j][x] = grid[j][x] + '*'
            foundedwords.append(word)

    #printgrid(grid)


def detectDiagonal(grid,x,y):

    for word in words:
        
        #go right down
        gridword = ""

        i_offset = 0
        for j in range(y, y + len(word)):
            if(j >= len(grid) or j < 0 or (x + i_offset) >= len(grid) or (x + i_offset) < 0):
                gridword = "outofindex"
                break
            if(j < len(grid) and j >= 0 ):
                gridword += grid[j][x + i_offset]
                i_offset += 1

        #print(gridword)
    
        if(gridword == word or gridword[::-1] == word):
            i_offset = 0
            for j in range(y, y + len(word)):
                grid[j][x + i_offset] = '_'
                i_offset += 1
            print("found: " + word)     
            foundedwords.append(word)


        #go left down
        gridword = ""

        i_offset = 0
        for j in range(y, y + len(word)):
            if(j >= len(grid) or j < 0 or (x - i_offset) >= len(grid) or (x - i_offset) < 0):
                gridword = "outofindex"
                break
            if(j < len(grid) and j >= 0 ):
                gridword += grid[j][x - i_offset]
                i_offset += 1

        #print(gridword)

        if(gridword == word or gridword[::-1] == word):
            i_offset = 0
            for j in range(y, y + len(word)):
                grid[j][x - i_offset] = '_'
                i_offset += 1
            print("found: " + word)  
            foundedwords.append(word)

    #printgrid(grid)


def detect(grid):

    for i in range(len(grid[0])):

        for j in range(len(grid)):          

            detectHorizontal(grid,i,j)
            detectVertical(grid,i,j)
            detectDiagonal(grid,i,j)

    printgrid(grid)


def printgrid(grid):
    output = ""
    for line in grid:
        for char in line:
            output += char + " "
        output += "\n"
    print(output)
    print("founded words : ")
    print(foundedwords)
    print("not founded words : "  + str(len(list(set(words) - set(foundedwords)))))
    print(list(set(words) - set(foundedwords)))
    for notfound in list(set(words) - set(foundedwords)):
        print(notfound)


def getkey():
    with open('gridbeforeL copy.txt') as file:
        lines = file.readlines()
        words = [line.rstrip() for line in lines]  
        key = ""
        for line in lines:
            s = "".join(line)
            s = s.replace("_", "")
            s = s.replace(" ", "")
            s = s.replace("\n", "")
            #print(s)
            key += s
            
        print(key)


if __name__ == '__main__':


    with open('gridbeforeL copy.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]  
        for line in lines:
            grid.append(line.split(" "))
    
    with open('words.txt') as file:
        lines = file.readlines()
        words = [line.rstrip() for line in lines]  

    #for words before L-pattern
    words = ["APPROA"]

    #detectDiagonal(grid,0,0)
    #detect(grid)

    getkey()
    