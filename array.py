from sys import maxint

# kadane's algorithm
def largest_sum_contiguous_sub_array(arr):
	max_so_far=arr[0]
	curr_max=arr[0]
	for a in arr[1:]:
		curr_max = max(a, curr_max+a)
		max_so_far = max(max_so_far, curr_max)
	return max_so_far

=========================================================================================================
#partition in 3 equal parts meaning each part should sum==sum(arr)/3. In a linear loop find it one by one 
def three_partition_array_equal_sum(arr, i, sum_all=sum(arr)):

#find a triplet in an array whose sum is closest to a given number

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

=========================================================================================================

def segregate_0_1(arr):
	start=0
	end=len(arr)-1
	while(start<end):
		while arr[start]==0: start+=1
		while arr[end]==1: end-=1
		arr[start],arr[end]=arr[end],arr[start]

#mid cant have 2 so no counter increament
def segregate_0_1_2(arr):
	lo=0
	mid=0
	hi=len(arr)-1
	while mid<=hi:
		if arr[mid]==0:
			arr[lo],arr[mid]=arr[mid],arr[lo]
			lo+=1
			mid+=1
		elif arr[mid]==1: mid+=1
		else:
			arr[mid],arr[hi]=arr[hi],arr[mid]
			hi-=1
segregate_0_1_2([2,0,1,0,1,2,2,0,1,0])

=========================================================================================================

#trapping rain water. Keep an array of larger building on the left side and an array of larger building on 
#the right side and then get the difference in indices
def trapping_rain_water(arr, l=len(arr)):
	if l<=2: return 0
	left_max,right_max,result=[0]*l,[0]*l,0
	left_max[0],right_max[0]=arr[0],arr[l-1]
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

=========================================================================================================

#Transform One String to Another using Minimum Number of Given Operation. BFS


#find k closest element to a given value
#sort the array then find the element using binary search and then move its right and left to get the closest element

#Find the smallest window in a string containing all characters of another string
#https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/


#Given an array A[] and a number x, check for pair in A[] with sum as x
#sort the array and then 

#Same can be used to get a triplet of a particular sum

#Shuffle a given array using Fisher Yates shuffle Algorithm

#Stock Buy Sell to Maximize Profit
#find the local minima and local maxima and substract it and do for remaining array
def stock_buy_sell(price):
	if len(price)<2: return
	buy,sell=[],[]
	i=0
	while i<len(price):
		while i<len(price)-1 and price[i+1]<=price[i]: i+=1
		if i==len(arr)-1: return
		buy.append(i+1)
		while i<len(price) and price[i]>=price[i-1]: i+=1
		sell.append(i-1)


def find_first_non_repeating_character_in_a_string():
	#use LinkedHashMap


#anagrams


