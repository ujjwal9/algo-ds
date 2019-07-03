#Topcoder has some good doc on dp
#Dp one way to think is of making 1D array of the total no like knapsack
#for recursion solution that requires to loop over all the values use cut rod algorithm
# Longest incresing subsequence(LIS), find min no perfect squares
#https://www.geeksforgeeks.org/variations-of-lis-dp-21/
#Lots of problem on LIS 
#Building bridges
#Maximum sum increasing subsequence
#The longest chain
#Box Stacking
#Always solve https://www.sanfoundry.com/dynamic-programming-problems-solutions/
#Longest zigzag sequence https://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493
#
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
	l = [[0]*(len(a1)+1) for i in xrange(len(a2)+1)]
	for i in xrange(len(a1)+1):
		for j in xrange(len(a2)+1):
			if a1[i-1]==a2[j-1]: l[i][j]=1+l[i-1][j-1]
			else l[i][j]=max(l[i-1][j], l[i][j-1])
	return l[len(a1)][len(a2)]

def edit_distance(w1,w2):
	n,m=len(w1),len(w2)
	dp=[0 for _ in xrange(m+1) for _ in xrange(n+1)]
	for i in xrange(n+1):
		for j in xrange(m+1):
			if i==0: dp[i][j]=m
			elif j==0: dp[i][j]=n
			elif w1[n-1]==w2[m-1]: dp[i][j]=dp[i-1][j-1]
			else dp[i][j]=1+min(dp[i][j-1] #replace
								dp[i-1][j] #insert
								dp[i-1][j-1] #replace
				)
#knapsack 0-1
def knapsack(W, wt, val, n):
	if n==0 or W==0: return 0
	if wt[n-1] > wt: return knapsack(W, wt, val, n-1)
	else max(val[n-1]+knapsack(W-wt[n-1], wt, val, n-1), knapsack(W, wt, val, n-1))

def knapsack_dp(W,wt,val,n):
	dp=[0]*(W+1)
	for i in xrange(len(wt)):
		for j in xrange(W, wt[i]-1,-1):
			dp[j]=max(dp[j],val[i]+dp[j-wt[i]])

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

#you can traverse down, right and lower diagonally till m,n all values positive
def min_cost_path(cost, m, n):
	dp[]=[[0 for _ in xrange(m+1) for _ in xrange(n+1)]]
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

#go through a loop for all the cases
def cut_rod(price, n):
	if n<=0: return 0
	max_value=-sys.maxint
	for i in xrange(0, n): max_value = max(max_value, price[i]+cut_rod(start, n-1-i))	
	return max_value

#precalculated values in dp
def cut_rod_dp(price):
	dp=[-sys.maxint for _ in xrange(len(arr)+1)]
	dp[0]=0
	for i in xrange(1, len(arr)+1):
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

#count number of ways to cover a distance with 1, 2 or 3 step
def ways(distance):
	dp=[0 for _ in xrange(distance+1)]
	dp[0],dp[1],dp[2]=1,1,2
	for i in xrange(3, distance): dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

#Tiling problem given 2xn board and 2x1 tile count no of ways to tile the board if the tile can be placed horizontally or vertically
def tiling(n):
	dp=[0 for i in xrange(n+1)]
	dp[0],dp[1]=1,1
	for i in xrange(2,n+1) dp[i]=dp[i-1]+dp[i-2]

#word break problem
public boolean wordBreak(String s, Set<String> wordDict) {
    int[] pos = new int[s.length()+1];
 
    Arrays.fill(pos, -1);
 
    pos[0]=0;
 
    for(int i=0; i<s.length(); i++){
        if(pos[i]!=-1){
            for(int j=i+1; j<=s.length(); j++){
                String sub = s.substring(i, j);
                if(wordDict.contains(sub)){
                    pos[j]=i;
                }
            } 
        }
    }
 
    return pos[s.length()]!=-1;
}

#How to print maximum number of A’s using given four keys
def max_a(n):
	if n<7: return n;
	dp[n+1]=[0]*(n+1)
	dp[1],dp[2],dp[3],dp[4],dp[5],dp[6]=1,2,3,4,5,6
	for i in xrange(7, n+1):
		for j in xrange(i-3,1,-1): dp[i]=max(dp[i], dp[j]*(i-j-1))


#longest bitonic sequence. Bitonic sequence are sequences which are first increasing then decreasing
#Make 2 arrays. First array inc[i] contains the no of increasing sequence till i and second decr[i]
#which contains no of decreasing sequence after i. Then sum up both 

#matrix chain multiplication. The dp version is an example of a diagonal dp which can be used
#to do any calculations which involve with the elements with all the subarray.
#Cuts in an array: digonal dp
def matrix_chain_multiplication(p,i,j):
	if i==j: return 0
	minn=sys.maxsize
	for k in xrange(i,j): #think of k as a seperator you put
		minn=min(minn, p[i-1]*p[k]*p[j]
			+matrix_chain_multiplication(p,i,k)
			+matrix_chain_multiplication(p,k+1,j))
	return minn

matrix_chain_multiplication(p,1,len(p))

#somewhat same as palindromic substring
def MatrixChainOrder(p, n): 
    for i in range(1, n): 
        m[i][i] = 0
    for L in range(1, n): 
        for i in range(n-L): 
            j = i+L
            m[i][j] = sys.maxint 
            for k in range(i, j): 
            	m[i][j] = max(m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j], m[i][j])
  
    return m[1][n-1]

#palindrome partitioning. https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/

# min_palindromic_partitions(arr, i, j) = Min {min_palindromic_partitions(arr,i,k)
#											   min_palindromic_partitions(arr,k+1,j)+1}
def min_palindromic_partitions_memoization(arr,i,j,map):
	if i>j: return 0
	
#word wrap
def word_wrap(arr, dp, N, i):
	if i > len(arr): return 0
	minn=0
	for j in xrange(N):
		if dp[i+j]: 
			minn=min(minn, word_wrap(arr,dp,N,i+j+1)+(N-j)^3)
	return minn

dp=[False]*(len(arr))
for i in arr:
	if i+1>len(arr) or arr[i+1]==' ': dp[i]=True
word_wrap(arr,dp,N,0)

#https://www.geeksforgeeks.org/mobile-numeric-keypad-problem/
#mobile numeric keyboard problem
#dfs on a graph. For memoization
def recursive(graph,c=0,N,num):
	global total
	if c==N: 
		total+=1
		return
	for i in graph[num]: recursive(graph,c+1,N,i)

graph={}
graph[0]=[0,8]
graph[1]=[1,2]
graph[2]=[1,2,5,3]
graph[3]=[2,3,6]
graph[4]=[1,4,5,7]
graph[5]=[2,4,5,6,8]
graph[6]=[3,5,6,9]
graph[7]=[4,7,8]
graph[8]=[5,7,8,9,0]
graph[9]=[6,8,9]

FLNE QXFA FC4W Y4
FLAH 2LHQ 	VL6K U4
