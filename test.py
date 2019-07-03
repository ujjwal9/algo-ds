arr=[[0,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
dp = [[0 for _ in xrange(len(arr))] for _ in xrange(len(arr))]
for i in xrange(len(arr)):
    dp[i][0]=arr[i][0]
    dp[0][i]=arr[0][i]
for i in xrange(1,len(arr)):
    for j in xrange(1,len(arr)):
        print i,j,dp[i-1][j-1]
        if arr[i-1][j]==1:
            dp[i][j]=min(arr[i][j-1],arr[i][j]==1,arr[i-1][j-1])
        else: dp[i][j]=0
result=0
print dp
for i in xrange(len(arr)):
    for j in xrange(len(arr)):
        result=max(result,dp[i][j])
print result