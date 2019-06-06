from sys import maxint

# kadane's algorithm
def largest_sum_contiguous_sub_array(arr):
	max_so_far=arr[0]
	curr_max=arr[0]
	for a in arr[1:]:
		curr_max = max(a, curr_max+a)
		max_so_far = max(max_so_far, curr_max)
	return max_so_far

#partition in 3 equal parts meaning each part should sum==sum(arr)/3. In a linear loop find it one by one 
def three_partition_array_equal_sum(arr, i, sum_all=sum(arr)):

#differnce in subset and partition
#simple backtracking problem
def k_subsets_array_equal_sum(arr,i,k,sum_all):


def subarray_of_non_negative_no_with_given_sum(arr, N):
	start=0
	s=arr[0]
	while i<len(arr):
		s=s+arr[i]
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
	one=1
	two=len(arr)-1
	while zero<one and one<two:
		while arr[zero]==0:zero+=1
		while arr[one]==1: one+=1
		while arr[two]==2: two-=1
		if zero<=one and one <= two:
			if (arr[one]==0 and (arr[zero]==1 or arr[zero]==2)): arr[zero],arr[one]=arr[one],arr[zero]
			if (arr[two]==0 and (arr[zero]==1 or arr[zero]==2)): arr[two],arr[zero]=arr[zero],arr[two]
			if arr[two]==1 and arr[one]==2: arr[one],arr[two]=arr[two],arr[one]	
	print arr
segregate_0_1_2([1,1,1,2,2,0,0,0,2,2,2,0,0,0,0,1,2,1,0,0,1])

#trapping rain water. Keep an array of larger building on the left side and an array of larger building on 
#the right side and then get the difference in indices
def trapping_rain_water(arr, l=len(arr)):
	if l<=2: return 0
	left_max,right_max,result=[0]*l,[0]*l,0
	for i in xrange(1,l): left_max[i]=max(left_max[i-1],arr[i])
	for i in xrange(l-2,-1,-1): right_max[i]=max(right_max[i+1],arr[i])
	for i in xrange(1,l-2): result+=min(left_max[i],right_max[i])-arr[i]


#largest rectangular area in a histogram. Same as trapping rain water. Like NGE problem use a stack to find 
#the nearest smaller right, left bar for bar then get the difference in indices
def next_smaller_element_right(arr):
	stak=[]
	result=[]
	for i in xrange(len(arr)-1,-1,-1):
		while stak and arr[stak[len(stak)-1]]>arr[i]: stak.pop()
		result[i]= stak[len(stak)-1] if stak else i
		stak.append(i)

def next_smaller_element_left(arr):
	stak=[]
	result=[]
	for i in xrange(0,len(arr)):
		while stak and arr[stak[len(stak)-1]]>arr[i]: stak.pop()
		result[i]=stak[len(stak)-1] if stak else i
		stak.append(i)

def largest_rectangular_area_histogram(arr, n=len(arr)):
	result=0
	left_min=next_smaller_element_left(arr)
	right_min=next_smaller_element_right(arr)
	for i in xrange(0,l):result=max(result,(right_min[i]-left_min[i]-1)*arr[i])

#Transform One String to Another using Minimum Number of Given Operation


#find k closest element to a given value
#sort the array then find the element using binary search and then move its right and left to get the closest element

#Find the smallest window in a string containing all characters of another string
#https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/
