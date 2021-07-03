#https://leetcode.com/discuss/general-discussion/1050391/must-do-dynamic-programming-problems-category-wise
#Topcoder has some good doc on dp. Dp one way to think is of making 1D array of the total no like knapsack
#for recursion solution that requires to loop over all the values use cut rod algorithm
#find min no perfect squares
http://people.csail.mit.edu/bdean/6.046/dp/
https://cp-algorithms.com
https://www.sanfoundry.com/dynamic-programming-problems-solutions/
https://www.freecodecamp.org/news/follow-these-steps-to-solve-any-dynamic-programming-interview-problem-cc98e508cd0e/
https://blog.usejournal.com/top-50-dynamic-programming-practice-problems-4208fed71aa3
#Longest incresing subsequence(LIS)
#https://www.geeksforgeeks.org/variations-of-lis-dp-21/
#Building bridges
#Maximum sum increasing subsequence
#The longest chain
#Box Stacking, russian doll, envelopes. do a sort by width,height increasing and then do LIS
#Longest zigzag sequence https://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493
#longest bitonic subsequence. for arr[i] do LIS till and LDS from arr[i] till end
#https://www.geeksforgeeks.org/weighted-job-scheduling/


#SUBSEQUENCE RELATED PROBLEMS
# for problems that require evaluating all subsets it could be solved by lis
def lis(a):
	d=[1]*len(a)
	for i in range(len(a)):
		for j in range(i):
			if a[j]<a[i]: d[i]=max(d[i],d[j]+1)

#longest common subsequence
def lcs(a1, a2):
	l = [[0]*(len(a1)+1) for i in range(len(a2)+1)]
	for i in range(len(a1)+1):
		for j in range(len(a2)+1):
			if a1[i-1]==a2[j-1]: l[i][j]=1+l[i-1][j-1]
			else l[i][j]=max(l[i-1][j], l[i][j-1])
	return l[len(a1)][len(a2)]

#longest repeating sequence. Same as lcs just that the same string is taken as the second input
def lrs(a):
	n=len(a)
	l = [[0]*(n+1) for i in range(n+1)]
	for i in range(n+1):
		for j in range(n+1):
			if a1[i-1]==a2[j-1]: l[i][j]=1+l[i-1][j-1]
			else l[i][j]=max(l[i-1][j], l[i][j-1])
	return l[n][n]

#LPS (Longest palindromic sequence)
#reverse the string and use lcs
	
************************************************************************************************************************************************

def edit_distance(w1,w2):
	n,m=len(w1),len(w2)
	dp=[0 for _ in range(m+1) for _ in range(n+1)]
	for i in range(n+1):
		for j in range(m+1):
			if i==0: dp[i][j]=j
			elif j==0: dp[i][j]=i
			elif w1[n-1]==w2[m-1]: dp[i][j]=dp[i-1][j-1]
			else dp[i][j]=1+min(dp[i][j-1] #delete
								dp[i-1][j] #insert
								dp[i-1][j-1]) #replace


#https://community.topcoder.com/stat?c=problem_statement&pm=5922&rd=8075
max(lis(a)+lis(reverse(a)))

#Given n jobs by start time, finish time, profit>=0, find max profit. problems that require evaluating all subsets: lis

def weighted_job_scheduling(arr,n=len(arr)):
	arr=sorted(arr, key=lambda x: x[1])
	dp=[0]*n
	for i in range(1,n):
		for j in range(i):
			if arr[j][0]<=arr[i][1]: dp[i]=max(dp[i], dp[j]+arr[i][2])


************************************************************************************************************************************************

#knapsack 0-1. Repitition not allowed to looping backwards 
#There are only two possibilities :
#1) We include the current item in the subset and recur for remaining items with remaining sum.
#2) We exclude current item from subset and recur for remaining items.
def knapsack(W,wt,val):
	dp=[0]*(W+1)
	for i in range(len(wt)):
		for j in range(W, wt[i]-1,-1):
			dp[j]=max(dp[j],val[i]+dp[j-wt[i]])

#unbounded knapsack. Repitition allowed
def unbounded_knapsack(W, wt, val):
	dp=[0]*(W+1)
	for i in range(W+1):
		for j in range(len(val)):
			if wt[j]<=i: dp[i]=max(dp[i], dp[i-wt[j]]+val[j])

#double knapsack
dp[i][w1_r][w2_r] = max( dp[i][w1_r][w2_r],
                    arr[i] + dp[i][w1_r - arr[i]][w2_r],
                    arr[i] + dp[i][w1_r][w2_r - arr[i]])


#fractional knapsack. Calculate value/weight ratio of all then sort and then start adding them 



#subset/Partition problem. Is there a subset with S sum
#given a set of non negative integers and a sum is there a subset with sum==given sum. 
def partition(arr, summ):
	if sum(arr)%2 != 0: return False
	middle=sum(arr)/2
	dp=[False]*(middle+1)
	for a in arr:
		for i in range(sum, a-1, -1):
			dp[i] = dp[i] or dp[i-a]
	return dp[middle+1]

#3 partition problem
#where we have two knapsacks each of capacity sum/3.
#Now we try to maximaze the items in these knapsacks.
def 3_partititon():
	par=sum/3
	dp[n + 1][par + 1][par + 1]
	if (sum % 3 != 0): return False
	for i in range(1, n+1):
        for j in range(1,p+1):
            for k in range(1,p+1):
                dp[i][j][k] = dp[i - 1][j][k];
                #keeping the item in the first knapsack
                if (j >= arr[i])
                    dp[i][j][k] = max(dp[i - 1][j - arr[i]][k] + arr[i], dp[i][j][k]);
                #keeping the item in the second knapsack
                if (k >= arr[i])
                    dp[i][j][k] = max(dp[i - 1][j][k - arr[i]] + arr[i], dp[i][j][k]);
    if(dp[n][par][par]==2*sum/3): return True

#Partition inito K equal sum subsets. Backtracking.
#https://www.techiedelight.com/k-partition-problem-print-all-subsets/
def subsetSum(S, n=len(S), sumLeft=[sum(S) // k] * k,  k):
    if checkSum(sumLeft, k): return True #each in sumleft should be 0
    if n < 0: return False
 	result = False
    for i in range(k):
        if not result and (sumLeft[i] - S[i]) >= 0:
            sumLeft[i] = sumLeft[i] - S[i]
            result = subsetSum(S, n - 1, sumLeft, A, k)
            sumLeft[i] = sumLeft[i] + S[i]
    return result

#there is a similar problem like above all that divide the array into k subarrays so that difference of sum os subarray will be minimized.

def cut_rod_dp(price, n):
	dp=[0]*(n+1)
	for i in range(1, n+1):
		for j in range(1,i+1):
			dp[i]=max(dp[i], price[j-1]+dp[i-j])

======================================================================================================================================
#coin exchange infinite coins N=4, S=[1,2,3] [1,1,1,1], [1,1,2] [1,3]	
def coin_exchange(N, S):
	dp=[0]*(N+1)
	for i in S: dp[i]=1
	for i in range(1, N+1):
		for c_value in S:
			if i-c_value>0:
				dp[i]=dp[i]+dp[i-c_value]

#minimum number of coins that make a given value
def min_coins(coins, N):
	dp=[sys.maxint]*(N+1)
	dp[0]=0
	for coin in coins: dp[coin]=1
	for i in range(1, N+1):
		for coin in coins:
			if coin<=i: dp[i]=min(dp[i],dp[i-coin]+1)

#count number of ways to cover a distance with 1, 2 or 3 step
def ways(distance):
	dp=[0 for _ in range(distance+1)]
	dp[0],dp[1],dp[2]=1,1,2
	for i in range(3, distance): dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

#Tiling problem given 2xn board and 2x1 tile count no of ways to tile the board if the tile can be placed horizontally or vertically
def tiling(n):
	dp=[0 for i in range(n+1)]
	dp[0],dp[1]=1,1
	for i in range(2,n+1) dp[i]=dp[i-1]+dp[i-2]

#https://www.geeksforgeeks.org/find-maximum-possible-stolen-value-houses/
def f(v,n=len(v)):
	dp=[0]*(n)
	dp[0]=v[0]
	dp[1]=max(v[0],v[1])
	for i in range(2,n):
		dp[i]=max(v[i]+dp[i-2],dp[i-1])
		
======================================================================================================================================
#count no of binary strings without consecutive 1's
def binary_strings(N):
	zero=[0]*(N+1)
	one=[0]*(N+1)
	a[1]=b[1]=1
	for i in range(N+1):
		one[i]=zero[i-1]
		zero[i]=zero[i-1]+one[z-1]
	return one[N]+zero[N]

#egg drop puzzle
def egg_drop(eggs, floor):
	if floor==0 or floor==1:return floor
	if eggs==1: return floor
	m=sys.maxint
	for f in range(1, floor+1):
		m = min(m,max(egg_drop(eggs-1, f-1), egg_drop(eggs, floor-f)))
	return m+1

def egg_drop_dp(eggs, floors):
	dp=[0 for _ in range(floors+1) for _ in range(eggs+1)]
	for i in range(1, floors+1): dp[1][i]=i
	for i in range(1, eggs+1): dp[i][1]=1
	for i in range(2, eggs+1):
		for j in range(2, floors+1):
			dp[i][j]=sys.maxint
			for x in range(1, j+1):
				dp[i][j] = min(dp[i][j], 1+max(dp[i-1][x-1],dp[i][j-x]))
	return dp[n][k]

#Painters partition problem
def partition(arr,n,k):
	if k==1: return sum(arr[0:n])
	if n==1: return arr[0]
	best=1000000000
	for i in range(1,n+1):
		best=min(best,max(partition(arr,i,k-1),sum(arr,i,n-1)))
	return best

def painters_partition_dp(arr,n,k):
	dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
	for i in range(1,k+1): dp[i][1]=arr[0]
	for i in range(1,n+1): dp[1][i]=sum(arr[0:i])
	for i in range(2,k+1):
		for j in range(2, n+1):
			best=1000000000
			for p in range(1,j+1):
				best=min(best,max(dp[i-1][p],sum(arr,p,j-1)))


======================================================================================================================================

#How to print maximum number of A s using given four keys
def max_a(n):
	if n<7: return n;
	dp[n+1]=[0]*(n+1)
	dp[1],dp[2],dp[3],dp[4],dp[5],dp[6]=1,2,3,4,5,6
	for i in range(7, n+1):
		for j in range(i-3,1,-1): dp[i]=max(dp[i], dp[j]*(i-j-1))

======================================================================================================================================

#longest bitonic sequence. Bitonic sequence are sequences which are first increasing then decreasing
#Make 2 arrays. First array inc[i] contains the no of increasing sequence till i and second decr[i]
#which contains no of decreasing sequence after i. Then sum up both 

#matrix chain multiplication(MCM) Diagonal dp
#Cuts in an array: digonal dp.
def mcm(p, n): 
	m=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(0, n): m[i][i] = 0
    for length in range(2, n): 
        for i in range(1,n-length+1): 
            j = i+length-1
            m[i][j]=sys.maxint
            for k in range(i, j): m[i][j] = max(m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j], m[i][j])
    return m[1][n-1]

#https://www.geeksforgeeks.org/mobile-numeric-keypad-problem/
#mobile numeric keyboard problem
#dfs on a graph. For memoization
def recursive(graph,c=0,N,num):
	global total
	if c==N: 
		total+=1
		return
	for i in graph[num]: recursive(graph,c+1,N,i)


===========================================================================================================================
#wildcard matching 
def wildcard(string, pattern, n, m):
	dp=[[False for _ in range(n+1)] for _ in range(m+1)]
	dp[0][0]=True
	for i in range(1, m):
		if pattern[i-1]=='*': dp[0][j]=dp[0][j-1]
	for i in range(1,n+1):
		for j in range(1,m+1):
			if pattern[j-1]=='?' or pattern[j-1]==string[i-1]:dp[i][j]=dp[i-1][j-1]
			else if pattern[j-1]=='*': dp[i][j]=dp[i][j-1] or dp[i-1][j]

===========================================================================================================================
#balloon burst
def max_coins(arr):
	if len(arr)==1: return arr[0]
	maxx=0
	for i in range(arr):
		s = 1 if i==0 else arr[i-1]
		e = 1 if i==len(arr)-1 else arr[i+1]
		maxx=max(maxx, max_coins(arr.remove(i) + s*arr[i]*e))
	return maxx

===========================================================================================================================
#jump game 
def f(jumps):
	n=len(jumps)
	dp=[0]*(n)
	dp[0]=1
	for i in range(n):
		for j in range(jumps[i]):
			if dp[i]+j<n: dp[dp[i]+j]=min(dp[dp[i]+j], dp[i]+j)

#jump game II

===========================================================================================================================
#Maximum sum such that no two elements are adjacent
def f(arr):
	incl,excl=0,0
	for i in arr:
		new_excl=max(excl,incl)
		incl=excl+i
		excl=new_excl
	return max(incl,excl)

===========================================================================================================================
#assembly line
def f():

#maximum sum when adjacent elements from the same list and same index value from different list cant be
def max_Sum( arr1, arr2, n=len(arr1)):
    dp[n][2]
    for i in range(n):
        if(i==0):
            dp[i][0] = arr1[i]; 
            dp[i][1] = arr2[i];           
       	else: 
       		dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + arr1[i]); 
       		dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + arr2[i]); 
    return max(dp[n-1][0], dp[n-1][1])

