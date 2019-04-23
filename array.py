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

def subarray_of_non_negative_no_with_given_sum(arr, N):
	start=0
	s=arr[0]
	while i<len(arr):
		s=s+i
		while s>N and start<i:
			s=s-arr[start]
			start+=1
		if s==N: return 1
		i+=1
	return 0

def segregate_0_1(arr):
	start=0
	end=len(arr)-1
	while(start<end):
		while arr[start]==0: start+=1
		while arr[end]==1: end-=1
		arr[start],arr[end]=arr[end],arr[start]

def segregate_0_1_2(arr):
	zero=0
	one=0
	two=len(arr)-1
	while (one<two):
		while arr[zero]==0:zero+=1
		while arr[one]==1: one+=1
		while arr[two]==2: two-=1
		if one<zero: one=zero
		if one < two:
			if arr[zero]==1 and arr[one]==0: arr[zero],arr[one]=arr[one],arr[zero]
			if (arr[two]==0  and (arr[zero]==1 or arr[zero]==2)): arr[two],arr[zero]=arr[zero],arr[two]
			if arr[one]==2 and arr[two]==1: arr[one],arr[two]=arr[two],arr[one]
	print arr

#trapping rain water



#Transform One String to Another using Minimum Number of Given Operation
