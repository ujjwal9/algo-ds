#coin game winner where 2 players have three choices.Pick 1 or x or y coins at a time. One who picks the last wins
#We can observe that A wins game for n coins only when it loses for coins n-1, n-x and n-y.
def winner(coins, x, y):
	dp=[False for _ in xrange(coins+1)]
	dp[0]=False
	dp[1]=True
	for i in xrange(2, coins+1):
		if i-1>0 and not dp[i-1]: dp[i]=True
		elif i-x>0 and not dp[i-x]: dp[i]=True
		elif i-y>0 and not dp[i-y]: dp[i]=True

#https://www.geeksforgeeks.org/optimal-strategy-for-a-game-dp-31/
#Row of coins of values v1...vn, n is even. Game is played in alternative turns where player either selects
#the first or the last coin left from the row. Maximum amount of money that we can definitely win if
#we start first
def game(arr, s, e):
	if s==e: return arr[s]
	if s<e: return 0
	return max(arr[s]+min(game(arr,s+2,e), game(arr,s+1, e-1)) 
		, arr[e]+min(game(arr,s,e-2), game(s-1,e-1)))

#tic tac toe minimax algo using evaluation or the heuristic function
def moves_left(board):
	for i in xrange(3):
		for j in xrange(3):
			if board[3][3]=='_': return True
	return False

def best_move(board):

def evaluate(board):
	#checking for rows:
	for row in xrange(3):
		if board[row][0]==board[row][1] and board[row][1]==board[row][2]:
			if board[row][0]==player: return 10
			else: return -10
	
	#checking for columns
	for col in xrange(3):
		if board[0][col]==board[1][col] and board[1][col]==board[2][col]:
			if board[0][col]==player: return 10
			else: return -10

	#checking for diagonals
	if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
		if board[1][1]==player: return 10
		else: return -10

	if board[0][2]==board[1][1] and board[1][1]==board[2][0]:
		if board[0][2]==player: return 10
		else: return -10 

	return 0

def minimax(board,depth,is_max):
	score=evaluate(board)
	if score==10 or score==-10: return score-depth
	if moves_left(board)==False: return 0-depth
	if is_max:
		best=-1000
		for i in xrange(3):
			for j in xrange(3):
				if board[i][j]=='_':
					board[i][j]=player
					best=max(best,minimax(board,depth+1,!is_max))
					board[i][j]='_'
		return best			
	else:
		best=1000
		for i in xrange(3):
			for j in xrange(3):
				if board[i][j]=='_':
					board[i][j]=opponent
					best=min(best,minimax(board,depth+1,!is_max))
					board[i][j]='_'
		return best



def find_best_move(board):
	best_val=-1000
	row,col=-1,-1
	for i in xrange(3):
		for j in xrange(3):
			if board[i][j]=='_':
				board[i][j]=player
				move_val=minimax(board,0,False)
				board[i][j]='_'
				if move_val>best_val: row,col,best_val=i,j,move_val
	print row, col

player, opponent= 'x', 'o'




