#make recursion not return the result but whether the current state is correct or not the 
#terminating condition should be the result bakctracking is_safe should be after for loop 
#ie it should be first checked if the solution is viable or not.
def permutation(str_arr, start, end): #abc, acb, bac, bca, cba, cab
	if(start==end-1): print ''.join(str_arr)
	else:
		for i in xrange(start, end):
			str_arr[start], str_arr[i] = str_arr[i], str_arr[start]
			permutation(str_arr, start+1, end)
			str_arr[start], str_arr[i] = str_arr[i], str_arr[start]

permutation(list("abc"), 0 , 3)


#this is not backtracking algo its simple recursion
def all_subsets(arr, str, i):
	if i==len(arr): 
		print str
		return
	all_subsets(arr, str+arr[i], i+1)
	all_subsets(arr, str, i+1)

==================================================================================================================================================

#rat in a maze. Source is (0,0) destination (N-1,N-1) rat can move only forward/down. 0 mean block is dead 1 means block can be used to go to destination.
def is_safe(maze, x, y):
	if x>=0 and x<N and y>=0 and y<M and maze[x][y]=1:return True
	return False

def rat_in_a_maze(maze, x, y, sol=[[0 for _ in xrange(N)] for _ in xrange(M)]):
	if x==N-1 and y==M-1: 
		sol[x][y]=1 #just used to marked the valid path
		return True
	if is_safe(maze, x, y):
		sol[x][y]=1
		if rat_in_a_maze(maze, x+1, y, sol) or rat_in_a_maze(maze, x, y+1, sol):
			return True
	sol[x][y]=0
	return False

==================================================================================================================================================

#The knight(horse) is placed at the first block of an empty board and must visit each square exactly once
def is_safe(x, y, chess):
	if x>=0 and x<8 and y>=0 and y<8 and chess[x][y]: return True
	return False


def knight_tour(x, y, chess, i):
	if i==64: return True
	for i in xrange(8):
		new_x,new_y=x+move[i],y+move[i]
		if is_safe(new_x, new_y, chess):
			chess[x][y]=True
			if knight_tour(new_x, new_y, chess, i+1): return True
	chess[x][y]=False
	return False		

move_x=[2, 1, -2, -1, 2, 1, -2, -1]
move_y=[1, 2, 1, 2, -1, -2, -1, -2]
chess=[[False] for _ in xrange(8) for _ in xrange(8)]

==================================================================================================================================================

#n queens problem expected output is a binary matrix that has 1s where queens are placed so that no 2 can attack each other
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

==================================================================================================================================================

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
			if sudoku(grid) == True: return True
		grid[row][col]=0
	return False

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



















