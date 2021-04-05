board = [
    [0,0,1, 0,0,0, 2,0,0],
    [3,0,2, 0,4,0, 0,0,5],
    [6,0,4, 0,0,5, 1,0,0],
    
    [0,0,6, 0,3,7 ,0,4,0],
    [0,0,8, 0,0,0, 5,0,0],
    [0,9,0, 1,8,0, 7,0,0],
    
    [0,0,7, 8,0,0, 4,0,9],
    [4,0,0, 0,2,0, 8,0,6],
    [0,0,5, 0,0,0, 3,0,0]
]


def solve(boardIterate):
    
    find = find_empty(boardIterate) # check if there are any empty/0 on the board
    if not find:
        return True
    else:
        row, col = find #find will return (i,j), the tuple which i will be row and col will be j
    
    for i in range(1,10): #checking all values from 1, 2,... 9 in the position. 
        if valid(boardIterate, i, (row, col)):  #checking if the number is valid in that empty position
            boardIterate[row][col] = i

            if solve(boardIterate): # recursion. Call solve() again but with boardIterate[row][col] = i.
                #Keep recursively try value until the board is solved
                return True #only return when the board is solved.

            boardIterate[row][col] = 0 #if the new value does not solve the board, it will backtrack and run the for-loop again, incrementing the number

    return False # when numbers have been exhausted and nothing works, the board is unsolvable 


def valid(boardIterate, number, position):
    # position will be the tuple of row, column. 
    # Check row
    for i in range(len(boardIterate[0])): #from 0 to total columns (values in the row)
        if boardIterate[position[0]][i] == number and position[1] != i:
            return False #return false if the number we submitted is the same row
    
    # Check column
    for i in range(len(boardIterate)): # from 0 to total rows in the board
        if boardIterate[i][position[1]] == number and position[0] != i:
            return False #return false if the number we submitted is the same as in the column
    
    # Check 3x3 square
    #box_x will show up which row we are on (0 means we are on the top, 1 means we are in the middle, and 2 means we are the last row)
    box_x = position[1] // 3 # integer division
    box_y = position[0] // 3
    

    for i in range (box_y * 3, box_y*3 + 3):
        for j in range (box_x * 3, box_x*3 + 3):
            if boardIterate[i][j] == number and (i,j) != position:
                return False
    return True


def print_board(boardIterate):
    #print(len(boardIterate))
    for i in range(len(boardIterate)): # for loop; going from 0 to total length of 'board', which is 9. Stops at 9. 
        #0, 1, 2,... 8 (essentially for (int i = 0; i < 9; i++))
        if i % 3 == 0 and i != 0: #if i is the third row, then print a line. Ignore the first line.
            print("-----------------------")
        
        for j in range(len(boardIterate[0])): # columns. Looking at total values/columns for the first row.
            if j % 3 == 0 and j != 0: # if column is the third but not the first
                print (" | ", end="") # print's end parameter disable newline

            if j == 8: # if last column then 
                print(boardIterate[i][j]) # By default Python print ends with newline.
            else:
                print(str(boardIterate[i][j]) + " ", end="") # Not the last column so it continue to print the value


def find_empty(boardIterate):
    # go orderly in the board/grid and look for the first 0. 
    # returns the tuple (i,j) of where the 0 is on the grid. 
    for i in range(len(boardIterate)):
        for j in range(len(boardIterate[0])):
            if boardIterate[i][j] == 0:
                return (i,j)

    return None 
                

print_board(board)
solve(board)
print("________________________")
print("SOLVED:")
print_board(board)