board = [
    [7,8,9,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],

    [0,0,7,0,4,0,2,6,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],

    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def valid(boardIterate, number, position):
    # Check row
    for i in range(len(boardIterate[0])):
        if boardIterate[pos[0]][i] == number and position[1] != i:
            return False

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
    for i in range(len(boardIterate)):
        for j in range(len(boardIterate[0])):
            if bo[i][j] == 0:
                return (i,j)
                

print_board(board)