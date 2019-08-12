# for matrix problem try to think of applying dfs or bfs

================================================================================================================================

#rotate a matrix by 90degree

#print a matrix diagonally

#print matrix spirally
def rec_matrix_n_x_m(start_row, start_col, end_row, end_col, matrix):
	for i in range(start_col, end_col): print matrix[start_row][i]
	for i in range(start_row+1, end_row): print matrix[i][end_col]
	for i in range(end_col-1, start_col, -1): print matrix[end_row][i]
	for i in range(end_row-1, start_row-1, -1): print matrix[i][start_col]
	rec_matrix_n_x_m(start_row+1, start_col+1, end_row-1, end_col-1, matrix)

================================================================================================================================

#largest sum square in a 2d matrix. find the largest reactangle and take the smaller index


#extension of kadane's algorithm
def largest_sum_rectangle_2d_matrix(arr):

#maximum size rectangle sub matrix with all 1s. find max histogram each row

#maximum size square sub matrix with all 1s. Dynamic programming
def f():
	for i in xrange(len(arr)): dp[i][0], dp[0][i]=arr[i][0],arr[0][i]
	for i in xrange(1,len(arr)):
	    for j in xrange(1,len(arr)):
	        if arr[i][j]==1: dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
	        else: dp[i][j]=0
	
================================================================================================================================

#flood fill algorithm. how to implement fill() in ms paint
def flood_fill(matrix,x,y,prevC,newC,M,N):
	if x<0 or x>=M or y<0 or y>=N or matrix[x][y]!=prevC: return
	matrix[x][y]=newC
	flood_fill(matrix,x,y+1,prevC,newC,M,N)
	flood_fill(matrix,x+1,y,prevC,newC,M,N)
	flood_fill(matrix,x,y-1,prevC,newC,M,N)
	flood_fill(matrix,x-1,y,prevC,newC,M,N)

#Given a matrix of ‘O’ and ‘X’, replace ‘O’ with ‘X’ if surrounded by ‘X’
def f(matrix):
	for i in xrange(len(matrix)):
		for j in xrange(len(matrix)):
			if matrix[i][j]=='O': matrix[i][j]='_'
	for i in xrange(len(matrix)):
		if matrix[0][i]=='_': flood_fill(matrix,0,i,'_','O',len(matrix),len(matrix))
		if matrix[i][len(matrix)-1]=='_': flood_fill(matrix,i,len(matrix)-1,len(matrix),len(matrix))
		if matrix[len(matrix)-1][i]=='_':flood_fill(matrix,len(matrix)-1,i,len(matrix),len(matrix))
		if matrix[i][0]=='_':flood_fill(matrix,i,0,len(matrix),len(matrix))

#Given a matrix of ‘O’ and ‘X’, find the largest subsquare surrounded by ‘X’. Same as maximum size rectangle matrix with all 1's
def f(matrix):
	dp=[[(0,0) for _ in xrange(len(matrix))] for _ in xrange(len(matrix))]
	dp[0][0]=(1,1) if matrix[0][0]=='X' else 0
	for i in xrange(1,len(matrix)):
		matrix[i][0]=(matrix[i-1][0]+1,1) if matrix[i][0]=='X' else (0,0)
		matrix[0][i]=(matrix[0][i-1]+1,1) if matrix[0][i]=='X' else (0,0)
	for i in xrange(1,len(matrix)):
		for j in xrange(1,len(matrix)):
			if matrix[i][j]=='X':(matrix[i][j-1]+1,matrix[i-1][j]+1)


#count no of islands where every island is row wise and column wise seperated.
#https://www.geeksforgeeks.org/count-number-islands-every-island-separated-line/
#find all top most cornors of the islands
def f(matrix):
	count=0
	for i in xrange(len(matrix)):
		for j in xrange(len(matrix[0])):
			if matrix[i][j]=='X' and (j==0 or matrix[i][j-1]=='O') and (i==0 or matrix[i-1][j]=='O'): count+=1

================================================================================================================================

#search an element in a row wise and column wise sorted matrix
def f(matrix, num):
	i,j=0,len(matrix[0])-1
	while i<len(matrix) and j>0:
		if matrix[i][j]==num: return(i,j)
		if matrix[i][j]<num:j-=1
		if matrix[i][j]>num:i+=1
	return (-1,-1)
	
#Print all elements in sorted order from row and column wise sorted matrix
#consider it as merging of k sorted array
#Find a common element in all rows of a given row-wise sorted matrix
#Kth smallest element in a row-wise and column-wise sorted 2D array
from heapq import heappush, heappop 
def f(matrix, k):
	l=[]
	n,m=len(matrix),len(matrix[0])
	for i in xrange(m): heapq.heappush(l,(matrix[0][i], (0,i)))	
	for i in xrange(k):
		node,vector=heapq.heappop()
		if vector[0]+1< n: heapq.heappush(matrix[vector[0]][vector[0]+1])

#A 2d matrix of 0 and 1 in which rows are sorted. You have to find the row number which has the Maximum number of 1.
#same as row wise and column wise start from top most if 1 move left if 0 move down
def f(matrix):
	i,j,n,m=0,len(matrix[0])-1,len(matrix),len(matrix[0])
	while i<n and j>=0:
		while j>=0 and arr[i][j]==1: j-=1
		while i<n and arr[i][j]==0: i+=1
	result m-j



================================================================================================================================
#Unique paths
def unique_paths(m,n):
	matrix=[[0 for _ in xrange(m)] for _ in xrange(n)]
	for i in xrange(n): matrix[i][0]=1
	for i in xrange(m): matrix[0][i]=1
	for i in xrange(1,n):
		for j in xrange(1,m): matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]

#Unique paths with obstacles. Obstacles are reperesented as 1 others as 0
def unique_paths(matrix):
	n,m=len(matrix), len(matrix[0])
	dp=[[0 for _ in xrange(m)] for _ in xrange(n)]
	dp[0][0] = 0 if matrix[0][0]==1 else 1
	for i in xrange(1,m): 
		if matrix[0][i]==0: dp[0][i]=dp[0][i-1]
	for i in xrange(1,n):
		if matrix[i][0]==0: dp[i][0]=dp[i-1][0]
	for i in xrange(1,n):
		for j in xrange(1,m):
			if matrix[i][j]==0: dp[i][j]=dp[i-1][j]+dp[i][j-1]


#minimum steps to reach at the end of a matrix. Given an array of integers where each element represents the max number of steps that can be made forward from that element
def f(matrix):
	m,n=len(matrix),len(matrix[0])
	dp=[[9999999 for _ in xrange(n)] for _ in xrange(m)]
	dp[0][0]=0
	for i in xrange(n):
		for j in xrange(m):
			if arr[i][j]+i<n: dp[i+arr[i][j]][j]=min(dp[i+arr[i][j]][j], dp[i][j]+1)
			if arr[i][j]+j<m: dp[i][j+arr[i][j]]=min(dp[i][j+arr[i][j]], dp[i][j]+1)
	return -1 if dp[i][j]==9999999 else dp[i][j]

#you can traverse down, right and lower diagonally till m,n all values positive
def min_cost_path(cost, m, n):
	dp[]=[[0 for _ in xrange(m+1) for _ in xrange(n+1)]]
	for i in xrange(1,n+1): dp[i][0]=cost[i-1][0]+dp[i-1][0]
	for i in xrange(1,m+1): dp[0][j]=cost[0][j-1]+dp[0][j-1]
	for i in xrange(1,n+1):
		for j in xrange(1,m+1): dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+cost[i,j]

#maximum sum path in a matrix.The maximum path is sum of all elements from first row to last row
#where you are allowed to move only down or diagonally to left or right
def f(matrix):
	r,c=len(matrix),len(matrix[0])
	res=0
	dp=[[0 for i in c] for i in xrange(r)]
	for i in xrange(c): dp[0][i]=matrix[0][i]
	for i in xrange(1,r):
		if (j>0 and j < c-1): mat[i][j]=max(mat[i-1][j], mat[i-1][j-1],mat[i-1][j+1])
        elif (j>0): mat[i][j]=max(mat[i-1][j],mat[i-1][j-1]) 
   		elif (j<c-1): mat[i][j]=max(mat[i-1][j], mat[i-1][j+1]) 
        res=max(mat[i][j],res) 

#longest increasing path in a matrix if only you can move to (i+1,j),(i,j+1)
def f(matrix):
	n,m=len(matrix),len(matrix[0])
	dp=[[1 for _ in xrange(m)] for _ in xrange(n)]
	for i in xrange(1,m): if matrix[0][i]>matrix[0][i-1]: dp[0][i]=dp[0][i-1]+1
	for i in xrange(1,n): if matrix[i][0]>matrix[i-1][0]: dp[i][0]=dp[i-1][0]+1
	for i in xrange(1,n):
		for j in xrange(1,m):
			if matrix[i][j]>matrix[i-1][j]: dp[i][j]=max(dp[i][j],dp[i-1][j]+1)
			if matrix[i][j]>matrix[i][j-1]: dp[i][j]=max(dp[i][j],dp[i][j-1]+1)


#longest increading path in a matrix if you can move in all four directions
#its increasing sequence so we dont have to maintain a visited array. just do a dfs
# memoization can also be used here
def dfs(i,j,n,m,matrix,l=1):
	global result
	result=max(result,l)
	if i+1<n and matrix[i+1][j]>matrix[i][j]: dfs(i+1,j,n,m,matrix,l+1)
	if i-1>=0 and matrix[i-1][j]>matrix[i][j]: dfs(i-1,j,n,m,matrix,l+1)
	if j+1<m and matrix[i][j+1]>matrix[i][j]: dfs(i,j+1,n,m,matrix,l+1)
	if j-1>=0 and matrix[i][j-1]>matrix[i][j]: dfs(i,j-1,n,m,matrix,l+1)

result=0
dfs(0,0,len(matrix),len(matrix[0]),matrix)

#Minimum time required to rot all oranges. BFS
def f(matrix):
	queue=[]
	result=0
	m,n=len(matrix[0]),len(matrix)
	for i in xrange(n):
		for j in xrange(m): 
			if matrix[i][j]=='R': queue.append((i,j))
	while queue:
		l=len(queue)
		for i in xrange(l):
			pop=queue.pop(0)
			x,y=pop[0],pop[1]
			if x+1<n and matrix[x+1][y]=='R':
				queue.append((x+1,y))
				matrix[x+1][y]='F'
			if x-1>0 and matrix[x-1][y]=='R':
				queue.append((x-1,y))
				matrix[x-1][y]='F'
			if y+1<m and matrix[x][y+1]=='R':
				queue.append((x,y+1))
				matrix[x][y+1]='F'
			if y-1<0 and matrix[x][y-1]=='R'
				matrix[x][y-1]='F'
		result+=1
	for i in xrange(n):
		for j in xrange(m):
			if matrix[i][j]=='R': return 9999999999
	return result

#count no of islands
#simple count no of connected components in an undirected graph. Either change the value 1 to something else as in rotten tomatoes 
#or keep a visited matrix
def dfs(visited,i,j,n,m,matrix):
	visited[i][j]=True
	if i+1<n and matrix[i+1][j]==1 and visited[i+1][j] is False: dfs(visited,i+1,j,n,m,matrix)
	if i-1>=0 and matrix[i-1][j]==1 and visited[i-1][j] is False: dfs(visited,i-1,j,n,m,matrix)
	if j+1<m and matrix[i][j+1]==1 and visited[i][j+1] is False: dfs(visited,i,j+1,n,m,matrix)
	if j-1>=0 and matrix[i][j-1]==1 and visited[i][j-1] is False: dfs(visited,i,j-1,n,m,matrix)
	if i+1<n and j-1>=0 and matrix[i+1][j-1]==1 and visited[i+1][j-1] is False: dfs(visited, i+1,j-1,n,m,matrix)
	if i+1<n and j+1<m and matrix[i+1][j+1]==1 and visited[i+1][j+1] is False: dfs(visited,i+1,j+1,n,m,matrix)
	if i-1<=0 and j-1<=0 and matrix[i-1][j-1]==1 and visited[i-1][j-1] is False: dfs(visited,i-1,j-1,n,m,matrix)
	if i-1<=0 and j+1<m and matrix[i-1][j+1]==1 and visited[i-1][j+1] is False: dfs(visited,i-1,j+1,n,m,matrix)

def f(matrix):
	n,m=len(matrix),len(matrix[0])
	visited=[[False for _ in xrange(m )] for _ in xrange(n)]
	result=0
	for i in xrange(n):
		for j in xrange(m):
			if matrix[i][j]==1 and visited[i][j] is False:
				dfs(visited,i,j,n,m,matrix)
				result+=1
	return result







