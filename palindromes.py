#Manachers algorithm

#https://www.geeksforgeeks.org/find-number-distinct-palindromic-sub-strings-given-string/

#longest palindromic substring
def lps(str): 
    n = len(str) 
    L = [[False for x in range(n)] for x in range(n)] 
    max_length=1
    start=0
    for i in range(n): L[i][i] = 1
    for k in range(2, n+1): 
        for i in range(n-k+1): 
            j=i+k-1
            if str[i] == str[j] and (L[i-1][j-1] or j-i==1):
            	L[i][j] = True
            	if k>max_length:
            		start=i
            		max_length=k

#Total palindromic substring
#Count the total number of True in longest palindromic substring
C = [0]*n
for i in range(n): 
    if (P[0][i] is True): 
            C[i] = 0; 
    else: 
        C[i] = sys.maxsize; 
        for j in range(i): 
            if(P[j + 1][i] == True and 1 + C[j] < C[i]): 
                C[i] = 1 + C[j]; 

#longest palindromic subsequence
dp = [0 for _ in xrange(n) for _ in xrange(n)]
for i in xrange(n): dp[i][i]=1
for k in xrange(2,n+1):
	for i in xrange(n-k+1):
		j=i+k-1
        if str[i] == str[j] or j-i==1: L[i][j] = L[i-1][j-1] + 2
        else: L[i][j] = max(L[i][j-1], L[i+1][j])

#Given a number, find the next smallest palindrome
def f(num):
    case1=True
    n=len(num)
    for i in xrange(num):
        if i!='9': case1=False
    if case1: return 1+'0'*(n-2)+1
    if n%2==0:
        
    else:
    