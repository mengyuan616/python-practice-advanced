#  File: sumMaze.py
#  Description: HW 8. 
#  Student's Name: Mengyuan Dong
#  Student's UT EID: md42252
#  Course Name: CS 313E 
#  Unique Number: 50739
#
#  Date Created: 04/16/2019
#  Date Last Modified: 04/19/2019

import copy

class State:

    def __init__(self,grid,gridRows,gridCols,startRow,startCol,endRow,endCol,\
                 history,value,goal):
        self.grid = grid
        self.gridRows = gridRows
        self.gridCols = gridCols
        self.startRow = startRow
        self.startCol = startCol
        self.endRow = endRow
        self.endCol = endCol
        self.history = history
        self.value = value
        self.goal = goal    

    # for printing out State objects for debugging
    def __str__(self):
        outStr = "   Grid:\n"
        for row in self.grid: # traverse through rows of grid
            outStr += "      "
            for item in row:
                if len(str(item)) == 1:
                    spaces = "    "
                elif len(str(item)) == 2: 
                    spaces = "   "
                else: 
                    spaces = "  "

                outStr += str(item) + spaces

            outStr += "\n"
   
        outStr += "   history: "+str(self.history)
        outStr += "\n   start point: ({:},{:})".format(self.startRow,\
                                                       self.startCol)
        outStr += "\n   sum so far: {:}\n".format(self.value)

        return outStr
        
# a function to see if a proposed move is a valid one.
def isValidMove(state,row,col):
    # if the move exceeds the grid
    if row < 0 or row >= state.gridRows or col < 0 or col >= state.gridCols:
        return False
    # if it's an X there
    elif state.grid[row][col] == "X":
        return False
    else:
        return True
        
    
# a function to recursively solve a maze represented by thisState
def solve(state):

    print("Is this a goal state?")

    # if thisState is a goal state:
    if state.value == state.goal and state.startRow == state.endRow and \
       state.startCol == state.endCol:
        print("Solution found!")
        return state.history
    
    # if the sum exceeds the target sum
    elif state.value > state.goal:
        print("No. Target exceeded:  abandoning path")
        return None
           
    # if the sum doesn't exceed the target sum
    else:    

        # try moving right
        print("No.  Can I move right?")
        if isValidMove(state,state.startRow,state.startCol+1):
            
            print("Yes!\nPaused...\n")

            # create a new State "one cell right" to the old position
            newState = State(copy.deepcopy(state.grid),state.gridRows,\
                             state.gridCols,state.startRow,state.startCol+1,\
                             state.endRow,state.endCol,copy.deepcopy\
                             (state.history),state.value,state.goal)
            
            # add the new location to history
            newState.history.append(newState.grid[newState.startRow]\
                                    [newState.startCol])
            
            # add current num to the sum
            newState.value += newState.grid[newState.startRow][newState.startCol]
            
            # change the current position in the grid to an "X" to show the move
            newState.grid[newState.startRow][newState.startCol] = "X"
            
            print("Problem is now:")
            print(newState)
                
            # recursively call solve using new instance 
            result = solve(newState)
            if result != None:
                return result
            

        print("No.  Can I move up?")
        if isValidMove(state,state.startRow-1,state.startCol):
            
            print("Yes!\nPaused...\n")

            # create a new State "one cell up" from the old position
            newState = State(copy.deepcopy(state.grid),state.gridRows,\
                             state.gridCols,state.startRow-1,state.startCol,\
                             state.endRow,state.endCol,copy.deepcopy\
                             (state.history),state.value,state.goal)
            
            # add the new location to history
            newState.history.append(newState.grid[newState.startRow]\
                                    [newState.startCol])
            
            # add current num to the sum
            newState.value += newState.grid[newState.startRow][newState.startCol]
            
            # change the current position in the grid to an "X" to show the move
            newState.grid[newState.startRow][newState.startCol] = "X"
            
            print("Problem is now:")
            print(newState)
                
            # recursively call solve using new instance 
            result = solve(newState)
            if result != None:
                return result
            

        print("No.  Can I move down?")
        if isValidMove(state,state.startRow+1,state.startCol):
            
            print("Yes!\nPaused...\n")

            # create a new State "one cell down" from the old position
            newState = State(copy.deepcopy(state.grid),state.gridRows,\
                             state.gridCols,state.startRow+1,state.startCol,\
                             state.endRow,state.endCol,copy.deepcopy\
                             (state.history),state.value,state.goal)
            
            # add the new location to history
            newState.history.append(newState.grid[newState.startRow]\
                                    [newState.startCol])
            
            # add current num to the sum
            newState.value += newState.grid[newState.startRow][newState.startCol]
            
            # change the current position in the grid to an "X" to show the move
            newState.grid[newState.startRow][newState.startCol] = "X"
            
            print("Problem is now:")
            print(newState)
                
            # recursively call solve using new instance 
            result = solve(newState)
            if result != None:
                return result
            

        print("No.  Can I move left?")
        if isValidMove(state,state.startRow,state.startCol-1):
            
            print("Yes!\nPaused...\n")

            # create a new State "one cell left" to the old position
            newState = State(copy.deepcopy(state.grid),state.gridRows,\
                             state.gridCols,state.startRow,state.startCol-1,\
                             state.endRow,state.endCol,copy.deepcopy\
                             (state.history),state.value,state.goal)
            
            # add the new location to history
            newState.history.append(newState.grid[newState.startRow]\
                                    [newState.startCol])
            
            # add current num to the sum
            newState.value += newState.grid[newState.startRow][newState.startCol]
            
            # change the current position in the grid to an "X" to show the move
            newState.grid[newState.startRow][newState.startCol] = "X"
            
            print("Problem is now:")
            print(newState)
                
            # recursively call solve using new instance 
            result = solve(newState)
            if result != None:
                return result
            
        # If none of the attempts succeed
        print("Couldn't move in any direction.  Backtracking.")
        return None


def main():

    maze = []
    rowNum = 0
    
    myFile = open("mazedata.txt","r")
    grid = []

    for line in myFile:
        line = line.strip()

        gridRow = line.split()

        for i in range(len(gridRow)):
            gridRow[i] = int(gridRow[i])

        if rowNum == 0:
            maze = gridRow
            rowNum += 1
        else:
            grid.append(gridRow)
    
    # read the first line and get the commands
    targetVal = int(maze[0])    # the target sum 
    gridRows = int(maze[1])       # the number of rows in the grid
    gridCols = int(maze[2])       # the number of columns in the grid
    startRow = int(maze[3])       # the row number of the start point
    startCol = int(maze[4])       # the column number of the start point
    endRow = int(maze[5])         # the row number of the end point
    endCol = int(maze[6])         # the column number of the end point

    # current state
    #value = grid[startRow][startCol]
    #history = [grid[startRow][startCol]]
    #grid[startRow][startCol] = None
    
    # set up the start state
    thisState = State(grid,gridRows,gridCols,startRow,startCol,endRow,endCol,\
                      [],0,targetVal)
    # add the this location to history
    thisState.history.append(thisState.grid[int(startRow)][int(startCol)])
    # add current num to the sum
    thisState.value = int(thisState.grid[int(startRow)][int(startCol)])
    # change the current position in the grid to an "X"
    thisState.grid[int(startRow)][int(startCol)] = "X"
    print(thisState)
    
    result = solve(thisState) # result will be None or the goal state's history

    if result == None:
        print("No solution exists")
    else:
        print("{:}".format(result))

main()
    
