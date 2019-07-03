# for matrix problem try to think of applying dfs or bfs
#rotate a matrix by 90degree

#print a matrix diagonally

#print matrix spirally
def rec_matrix_n_x_m(start_row, start_col, end_row, end_col, matrix):
	for i in range(start_col, end_col): print matrix[start_row][i]
	for i in range(start_row+1, end_row): print matrix[i][end_col]
	for i in range(end_col-1, start_col, -1): print matrix[end_row][i]
	for i in range(end_row-1, start_row-1, -1): print matrix[i][start_col]
	rec_matrix_n_x_m(start_row+1, start_col+1, end_row-1, end_col-1, matrix)

#largest sum square in a 2d matrix. find the largest reactangle and take the smaller index


#extension of kadane's algorithm
def largest_sum_rectangle_2d_matrix(arr):

#maximum size rectangle sub matrix with all 1s. find max histogram each row

#maximum size square sub matrix with all 1s. Dynamic programming
def f():
	for i in xrange(len(arr)):
    dp[i][0], dp[0][i]=arr[i][0],arr[0][i]
	for i in xrange(1,len(arr)):
	    for j in xrange(1,len(arr)):
	        if arr[i-1][j]==1: dp[i][j]=min(arr[i][j-1],arr[i][j]==1,arr[i-1][j-1])
	        else: dp[i][j]=0
	

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



#search an element in a row wise and column wise sorted matrix
#start with the last element in the first row
def f(matrix):

#Print all elements in sorted order from row and column wise sorted matrix
#consider it as merging of k sorted array
#minimum steps to reach at the end of a matrix
def f(matrix):


#maximum sum path in a matrix

#Kth smallest element in a row-wise and column-wise sorted 2D array
#same as finding a kth smallest element in a set of sorted arrays

#A 2d matrix of 0 and 1 in which rows are sorted. You have to find the row number which has the Maximum number of 1.
#same as row wise and column wise start from top most if 1 move left if 0 move down

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

