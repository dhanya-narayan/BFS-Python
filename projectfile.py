import os
import queue
import pprint
import sys, getopt
from pprint import pprint
print ("enter input file")
filestdin = input()
with open(sys.argv[1], 'r') as filestdin:
    string = filestdin.read()
print("enter output file")
filestdout = input()
fileout = open(filestdout, "w")
#print(string)
string = string.replace(" ","")
#print(string)
#create a grid using strings 
grid = []
grid.append((string[0:10]))
grid.append((string[10:20]))
grid.append((string[20:30]))
grid.append((string[30:40]))
grid.append((string[40:50]))
grid.append((string[50:60]))
grid.append((string[60:70]))
grid.append((string[70:80]))
grid.append((string[80:90]))
grid.append((string[90:100]))
pprint(grid)
#print path in console using BFS and expanding shallowest node first
def Path(grid, path=""):
    for x, position in enumerate(grid[0]):
        if position == "1":
            start = x
    movesList = []
    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i-=1
            movesList.append("left")
            print("left", file = fileout)
        elif move == "R":
            i+=1
            movesList.append("right")
            print("right", file=fileout)
        elif move == "U":
            j-=1
            movesList.append("up")
            print("up", file = fileout)
        elif move == "D":
            j+=1
            movesList.append("down")
            print("down", file = fileout)
        position.format((j,i))
    fileout.close()
    print(movesList)
    return movesList
#decide valid moves
def validmove(grid, moves):
    for x, position in enumerate(grid[0]):
        if position == "1":
            start = x
    i = start
    j = 0
    for move in moves:
        if move == "L":
            i-=1
        elif move == "R":
            i+=1
        elif move == "U":
            j-=1
        elif move == "D":
            j+=1
        if not(0 <= i < len(grid[0]) and 0 <= j < len(grid)):
            return False
        elif(grid [j][i] == "3"):
            return False
    return True
#find goal of maze
def endval(grid, moves):
    for x, position in enumerate(grid[0]):
        if position == "1":
            start = x
    i = start
    j = 0
    for move in moves:
        if move == "L":
            i-=1
        elif move == "R":
            i+=1
        elif move == "U":
            j-=1
        elif move == "D":
            j+=1
    if grid[j][i] == "2":
        Path(grid, moves)
        return True
    return False

mainalg = queue.Queue()
#pop visited nodes in the queue after BFS traversal
mainalg.put("")
add = ""
while not endval(grid, add):
    add = mainalg.get()
    for j in ["L","R","U","D"]:
        put = add+j
        if validmove(grid,put):
            mainalg.put(put)
   
