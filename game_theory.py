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
