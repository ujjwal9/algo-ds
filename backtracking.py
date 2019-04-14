#make recursion not return the result but the terminating condition should be the result
#bakctracking is_safe should be after for loop ie it should be first checked if the 
# solution is viable or not or first recur with the values and then for each value it
# should first check if the value is safe or not. So always first check and recut for 
# only the valid values as it also makes more sense
def permutation(str_arr, start, end):
	if(start==end-1): 
		print ''.join(str_arr)
	else:
		for i in xrange(start, end):
			str_arr[start], str_arr[i] = str_arr[i], str_arr[start]
			permutation(str_arr, start+1, end)
			str_arr[start], str_arr[i] = str_arr[i], str_arr[start]

permutation(list("abc"), 0 , 3)

#rat in a maze
def is_safe(maze, x, y):
	if x>=0 and x<N and y>=0 and y<M and maze[x][y]=1:return True
	return False

def rat_in_a_maze(maze, x, y, sol=[[0 for _ in xrange(N)] for _ in xrange(M)]):
	if x==N-1 and y==M-1: 
		sol[x][y]=1
		return True
	if is_safe(maze, x, y):
		sol[x][y]=1
		if rat_in_a_maze(maze, x+1, y, sol) or rat_in_a_maze(maze, x, y+1, sol):
			return True
	sol[x][y]=0
	return False

#The knight(horse) is placed at the first block of an empty board and must visit each square exactly once
def is_safe(x, y, chess):
	if x>=0 and x<8 and y>=0 and y<8 and chess[x][y]: return True
	return False


def knight_tour(x, y, move_x, move_y, chess, i):
	if i==64:
		print i 
		return True
	if is_safe(x, y, chess):
		chess[x][y]=True
		valid_square=True
		for i in xrange(8):
			valid_square = valid_square or knight_tour(x+move_x[i], y+move_y[i], move_x, move_y, chess, i+1)
			if valid_square: return True
	chess[x][y]=False
	return False		


move_x=[2, 1, -2, -1, 2, 1, -2, -1]
move_y=[1, 2, 1, 2, -1, -2, -1, -2]
chess=[[False] for _ in xrange(8) for _ in xrange(8)]

#n queens problem expected output is a binary matrix that has 1s where queens are placed so that no
#2 can attack each other
#trick is to try placing each queen in each column if position is wrong then recur for another one
def is_safe(row, col, board):
	for i in xrange(y):
		if board[i][y]==1: return False

	#check for diagonal up

	#check for diagonal down

def n_queens(board, col):
	if col >= N : return True
	for row in xrange(N):
		if is_safe(row, col, board):
			if n_queens(board, col+1) == True: 
				return True
			board[row][col]=0
	return False

N=4
board=[[-1 for _ in xrange(N)] for _ in xrange(N)]

#sudoku
#get an unassigned row,col and try for all valid values
def is_safe(grid, x, y, n):
	#check if the number is present in the square
	#check if the number is present in the row
	#check if the number is present in the column

def uassigned_location(grid):
	for row in xrange(9):
		for col in xrange(9):
			if grid[row][col] == 0:
				return row,col
	return -1,-1

def sudoku(grid):
	row,col = uassigned_location()
	if row==-1 and col==-1: return True
	for n in xrange(1, 10):
		if is_safe(grid, row, col, n)
			grid[row][col]=n
			if sudoku(grid) == True
				return True
		grid[row][col]=0
	return False

grid=[[0 for _ in xrange(9)] for _ in xrange(9)]
grid =   [[3,0,6,5,0,8,4,0,0], 
          [5,2,0,0,0,0,0,0,0], 
          [0,8,7,0,0,0,0,3,1], 
          [0,0,3,0,1,0,0,8,0], 
          [9,0,0,8,6,3,0,0,5], 
          [0,5,0,0,9,0,6,0,0], 
          [1,3,0,0,0,0,2,5,0], 
          [0,0,0,0,0,0,0,7,4], 
          [0,0,5,2,0,6,3,0,0]] 

#tug of war



















