#rotate a matri by 90degree

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


#maximum size square sub matrix with all 1s. Dynamic programming

#maximum size rectangle sub matrix with all 1s. find max histogram each row

#Given a matrix of ‘O’ and ‘X’, find the largest subsquare surrounded by ‘X’. Same as maximum size rectangle matrix with all 1's

#search an element in a row wise and column wise matrix
#start with the last element in the first row

#minimum steps to reach at the end of a matrix

#maximum sum path in a matrix

