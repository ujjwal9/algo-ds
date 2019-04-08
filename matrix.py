#maximum sum rectangle in a 2d matrix

#print matrix spirally
def rec_matrix_n_x_m(start_row, start_col, end_row, end_col, matrix):
	for i in range(start_col, end_col): print matrix[start_row][i]
	for i in range(start_row+1, end_row): print matrix[i][end_col]
	for i in range(end_col-1, start_col, -1): print matrix[end_row][i]
	for i in range(end_row-1, start_row-1, -1): print matrix[i][start_col]
	rec_matrix_n_x_m(start_row+1, start_col+1, end_row-1, end_col-1, matrix)

