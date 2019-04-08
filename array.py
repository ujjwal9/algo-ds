from sys import maxint

# kadane's algorithm
def largest_sum_contiguous_sub_array(arr):
	max_so_far=arr[0]
	curr_max=arr[0]
	for a in arr:
		curr_max = max(a, curr_max+a)
		max_so_far = max(max_so_far, curr_max)
	return max_so_far

def three_partition_array_equal_sum(arr, i, sum_all=sum(arr)):
	if i==(len(arr)-1): return arr[i]
	sum1,sum2=0,0
	for i in xrange(len(arr)):
		for j in xrange(i+1, len(arr)):
			sum1=three_partition_array_equal_sum(arr, i)
			sum2=three_partition_array_equal_sum(arr, j)
			if sum1==sum2 and sum2==(sum_all-(sum1+sum2)): print sum1
	return sum1
