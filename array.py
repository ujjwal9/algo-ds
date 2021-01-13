from sys import maxint
#Bi directional sweep. There could be 2 ways of doing the sweep. Either move both at once in a loop or use 3 loops and move individually uptil its limit.

# kadane's algorithm
def largest_sum_contiguous_sub_array(arr):
	max_so_far,curr_max=sys.minint,sys.minint
	for a in arr:
		curr_max = max(a, curr_max+a)
		max_so_far = max(max_so_far, curr_max)
	return max_so_far

=========================================================================================================

#2sum. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
def twoSum(nums, target):
	d={}
    d[nums[0]]=0
    for i in xrange(1, len(nums)):
        if (target-nums[i]) in d: return [i,d[target-nums[i]]]
        d[nums[i]]=i

#2sumII. Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
def twoSum2(numbers, target):
    l,r=0,len(numbers)-1
    while l<r:
    	a=numbers[l]+numbers[r]
        if a>target: r-=1
        elif a<target: l+=1
    	else: return [l+1,r+1]

#3sum. Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
def threeSum(nums):
    res=[]
    nums.sort()
    for i in xrange(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]: #handling duplicates at level 1
            i+=1
            continue
        l,r=i+1,len(nums)-1
        while l<r:
            two_sum=nums[l]+nums[r]
            if two_sum+nums[i]>0: r-=1
            elif two_sum+nums[i]<0: l+=1
            else: 
                res.append([nums[i],nums[l],nums[r]])
                l+=1
                while nums[l] == nums[l-1] and l < r: l+=1 # handling duplicate at level 2
    return res

#4sum. Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
def foursum(nums):
	result=[]
	nums.sort()
	for i, a in enumerate(nums): 
		if i>0 and a==nums[i-1]: continue
		new_target= target-a
		result += threeSum(nums[index + 1:], new_target)
	return result

#Subarray sum equals k. Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k. sum(i,j)=sum(0,j)-sum(0,i)
#this is done by cummulative sum in O(n)
def subarraySum(nums, k):
    s = 0
    sum_idx = {}
    sum_idx[0] = 1
    res = 0;
    for n in nums : 
        s += n
        sum_arr.append(s)
        if (s - k) in sum_idx : 
        	res += sum_idx[s - k]
        if s in sum_idx :
            sum_idx[s] += 1
         else : 
            sum_idx[s] = 1
    return res

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

#largest rectangular in a histogram. Like NGE problem use a stack to find the nearest smaller right, left bar for bar then get the difference in indices
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


#container with most water
def maxArea(self, height: List[int]) -> int:
	res = 0
	l, r = 0, len(height) - 1
	while l < r:
		area = (r - l) * min(height[l], height[r])
		res = max(res, area)
		if height[l] < height[r]: l += 1
		else:r -= 1
	return res

#maximum rectangle



=========================================================================================================

#Given an arraay of positive integers find one triplet such that indexes are in increasing order so as values at index. i<j<k and a[i]<a[j]<a[k] in O(n)
def find_smaller_j(arr):
	arr_i=[-1]*len(arr)
	minn=0
	for i in xrange(1,len(arr)):
		if arr[i-1]<arr[minn]:minn=i-1
		if arr[minn]<arr[i]: arr_i[i]=minn
	result arr_i

def find_bigger_j(arr):
	arr_k=[-1]*len(arr)
	maxx=1
	for i in xrange(len(arr)-2,-1,-1):
		if arr[i+1]>arr[maxx]:maxx=i+1
		if arr[maxx]>arr[i]: arr_k[i]=maxx
	return arr_k

def f(arr):
	result=None
	arr_i=find_smaller_j(arr)
	arr_k=find_bigger_j(arr)
	for j in xrange(2,len(arr)-1):
		if arr_i[j]!=-1 and arr_k[j]!=-1: result=(arr(arr_i[j]),arr[j],arr_k[j])

=========================================================================================================
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

=========================================================================================================

def segregate_0_1(arr):
	start=0
	end=len(arr)-1
	while(start<end):
		while arr[start]==0: start+=1
		while arr[end]==1: end-=1
		arr[start],arr[end]=arr[end],arr[start]

#all logic on mid
def segregate_0_1_2(arr):
	lo,mid,hi=0,0,len(arr)-1
	while mid<=hi:
		if arr[mid]==0:
			arr[lo],arr[mid]=arr[mid],arr[lo]
			lo+=1
			mid+=1
		elif arr[mid]==1: mid+=1
		else:
			arr[mid],arr[hi]=arr[hi],arr[mid]
			hi-=1 #new arr[mid] could be 0 also
segregate_0_1_2([2,0,1,0,1,2,2,0,1,0])

=========================================================================================================

#find k closest element to a given value
#sort the array then find the element using binary search and then move its right and left to get the closest element

#Find the smallest window in a string containing all characters of another string
#https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/
#two pointers problem

#Shuffle a given array using Fisher Yates shuffle Algorithm

def find_first_non_repeating_character_in_a_string():
	#use LinkedHashMap


#anagrams

#next greater element.find the first element arr[i-1]<arr[i] then swap it with the lowest element
#greater than arr[i-1] and then sort the arr[i:]
def f(num):
	n=len(num)
	i=n-1
	while i>0 and num[i-1]>num[i]: i-=1
	if i==0: return num
	less=i
	for j in xrange(i+1, n):
		if arr[j]>num[i-1] and arr[j]<arr[less]: less=j
	arr[i],arr[less]=arr[less],arr[i]
	arr[i:].sort()

#maximum length of string sub string that is not palindrome
#cases : all alphabets are same: 0
#if first and last are not same then n else n-1

=========================================================================================================

def pascal( row):
	p = [[1 for _ in xrange(i+1)] for i in xrange(row+1)]
	for i in xrange(2,row+1):
		for j in xrange(1,i):
			p[i][j]=p[i-1][j-1]+p[i-1][j]




