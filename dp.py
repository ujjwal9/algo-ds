#Dp one way to think is of making 1D array of the total no like knapsack
# Longest incresing subsequence(LIS), find min no perfect squares
def lis(arr, n):
	if n==1: return 1
	max_ending_here=1
	for i in xrange(1, n):
		l=lis(arr, i)
		if arr[i-1] < arr[n-1]: max_ending_here = max(max_ending_here, l+1)
	return max_ending_here

def lis_dp(arr):
	lis=[1]*len(arr)
	for i in xrange(1, n):
		for j in xrange(0, i):
			if arr[j]<arr[i] and lis[i]<lis[j]+1 : 
				lis[i]=lis[j]+1

def lcs(a1, a2. m, n):
	if m==0 or n==0: return 0
	elif a1[m-1] == a2[n-1]: return 1+lcs(a1, a2, m-1, n-1)
	return max(lcs(a1, a2, m-1,n), lcs(a1, a2, m, n-1))

def lcs_dp(a1, a2):
	l = [[None]*(len(a1)+1) for i in xrange(len(a2)+1)]
	for i in xrange(len(a1)+1):
		for j in xrange(len(a2)+1):
			if i==0 or j==0: l[i][j]=0
			elif a1[i-1]==a2[j-1]: l[i][j]=1+l[i-1][j-1]
			else l[i][j]=max(l[i-1][j], l[i][j-1])
	return l[len(a1)][len(a2)]

#knapsack 0-1
def knapsack(W, wt, val, n):
	if n==0 or W==0: return return 0
	if wt[n-1] > wt: return knapsack(W, wt, val, n-1)
	else max(val[n-1]+knapsack(W-wt[n-1], wt, val, n-1), knapsack(W, wt, val, n-1))

def knapsack_dp(W, wt, val, n):
	dp = [[None]*(W+1) for i in xrange(n+1)]
	for i in xrange(N+1):
		for w in xrange(W+1):
			if i==0 or w==0: dp[i][w]=0
			elif wt[i-1]<=w: dp[i][w]=max(dp[i-1][w], dp[i-1][w-wt[i-1]]+val[i-1])
			else: dp[i][w]=dp[i-1][w]

#unbounded knapsack
def unbounded_knapsack(W, wt, val, n):
	dp=[0 for i in xrange(W+1)]
	for i in xrange(W+1):
		for j in xrange(n):
			if wt[j]<=i: dp[i] = max(dp[i], dp[i-wt[j]]+val[j])

#coin exchange infinite coins N=4, S=[1,2,3] [1,1,1,1], [1,1,2] [1,3]	
def coin_exchange(N, S):
	dp=[0]*(N+1)
	for i in S: dp[i]=1
	for i in xrange(1, N+1):
		for c_value in S:
			if i-c_value>0:
				dp[i]=dp[i]+dp[i-c_value]

#minimum number of coins that make a given value
def min_coins(coins, N):
	dp=[sys.maxint]*(N+1)
	dp[0]=0
	for coin in coins: dp[coin]=1
	for i in xrange(1, N+1):
		for coin in coins:
			if coin<=i: dp[i]=min(dp[i],dp[i-coin]+1)

#you can traverse down, right and lower diagonally till m,n
def min_cost_path(cost, m, n):
	dp[]=[[0 for _ in xrange(m+1) for _ in xrange(n+1)]]
	for i in xrange(m+1): dp[0][i]=cost[0][m]+dp[0][m-1]
	for i in xrange(n+1): dp[n][0]=cost[n][0]+dp[n-1][0]
	for i in xrange(1,m+1):
		for j in xrange(1,n+1):
			dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+cost[i,j]

#count no of binary strings without consecutive 1's
def binary_strings(N):
	zero=[0]*(N+1)
	one=[0]*(N+1)
	a[1]=b[1]=1
	for i in xrange(N+1):
		one[i]=zero[i-1]
		zero[i]=zero[i-1]+one[z-1]
	return one[N]+zero[N]

#egg drop puzzle
def egg_drop(eggs, floor):
	if floor==0 or floor==1:return floor
	if eggs==1: return floor
	m=sys.maxint
	for f in xrange(1, floor+1):
		m = min(max(egg_drop(eggs-1, f-1), egg_drop(eggs, floor-f)), m)
	return m+1

def egg_drop_dp(eggs, floors):
	dp=[0 for _ in xrange(floors+1) for _ in xrange(eggs+1)]
	for i in xrange(1, floors+1): dp[1][i]=i
	for i in xrange(1, eggs+1): dp[i][1]=1
	for i in xrange(2, eggs+1):
		for j in xrange(2, floors+1):
			dp[i][j]=sys.maxint
			for x in xrange(1, j+1):
				dp[i][j] = min(dp[i][j], 1+max(dp[i-1][x-1],dp[i][j-x]))
	return dp[n][k]

def cut_rod(price, n):
	if n<=0: return 0
	max_value=-sys.maxint
	for i in xrange(start, end): max_value = max(max_value, price[i]+cut_rod(start, n-1-i))	
	return max_value

def cut_rod_dp(price, n):
	dp=[-sys.maxint for _ in xrange(n+1)]
	dp[0]=0
	for i in xrange(1, n+1):
		for j in xrange(i):
			dp[i]=max(dp[i], price[j]+dp[i-j-1])

#all the questions where considering all subsets of an array is required use dp[n+1][sum+1]
#given a set of non negative integers and a sum is there a subset with sum==given sum
#this is a NP Complete problem but we can solve it in pseudo polynomial time
def subset_sum(arr, summ):
	# n>0
	n=len(arr)
	dp=[[False for _ in xrange(summ+1)] for _ in xrange(n+1)]
	for i in xrange(n+1): dp[i][0]=True
	for i in xrange(1,summ+1): dp[0][i]=False
	for i in xrange(1,n+1):
		for j in xrange(1,summ+1):
			if j<arr[i-1]: dp[i][j]=False
			if j>=arr[i-1]: dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]


#Minimum sum partition non negative integers
def min_sum_partition(arr):
	subset_sum(arr, sum(arr))
	#for sum/2 find nearest True






