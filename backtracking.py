#make recursion not return the result but the terminating condition should be the result
def permutation(str_arr, start, end):
	if(start==end-1): 
		print ''.join(str_arr)
	else:
		for i in xrange(start, end):
			str_arr[start], str_arr[i] = str_arr[i], str_arr[start]
			permutation(str_arr, start+1, end)
			str_arr[start], str_arr[i] = str_arr[i], str_arr[start]

permutation(list("abc"), 0 , 3)

def is_safe(maze, x, y):
	if x>=0 and x<N and y>=0 and y<M and maze[x][y]=1:return True
	return False

def rat_in_a_maze(maze, x, y, sol=[[0 for _ in xrange(N)] for _ in xrange(M)]):
	if x==N-1 and y==M-1: 
		sol[x][y]=1
		return True
	if is_safe(maze, x, y):
		sol[x][y]=1
		if rat_in_a_maze(maze, x+1, y, sol) or rat_in_a_maze(maze, x, y+1, sol):
			return True
	sol[x][y]=0
	return False

