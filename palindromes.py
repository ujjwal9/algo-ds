#Manachers algorithm

#https://www.geeksforgeeks.org/find-number-distinct-palindromic-sub-strings-given-string/

#longest palindromic substring
def lps(str): 
    n = len(str) 
    L = [[False for x in range(n)] for x in range(n)] 
    max_length=1
    start=0
    for i in range(n): 
        L[i][i] = 1
    for k in range(2, n): 
        for i in range(n-k): 
            j=i+k-1
            if (L[i-1][j-1] or j-i==1) and str[i] == str[j]:
            	L[i][j] = True
            	if k>max_length:
            		start=i
            		max_length=k

#Total palindromic substring
#Count the total number of True in longest palindromic substring
def rec(str,i,j):
    if i==j: return 0
    if i+1==j and str[i]==str[j]: return 0 
    minn = 0
    for k in xrange(i+1,j): minn=min(rec(str,i,k), rec(k+1,j))+1
    return 0 if minn==2 else minn

#longest palindromic subsequence
dp = [0 for _ in xrange(n) for _ in xrange(n)]
for i in xrange(n): dp[i][i]=1
for k in xrange(2,n+1):
	for i in xrange(n-k+1):
		j=i+k-1
        if str[i] == str[j]: L[i][j] = L[i+1][j-1] + 2
        else: L[i][j] = max(L[i][j-1], L[i+1][j])

# min_palindromic_partitions(arr, i, j) = Min {min_palindromic_partitions(arr,i,k)
#                                              min_palindromic_partitions(arr,k+1,j)+1}
def min_palindromic_partitions_memoization(arr,i,j,map):
    if i>j: return 0
    