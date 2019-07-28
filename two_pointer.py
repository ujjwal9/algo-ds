#find triplets whose sum is zero
def f(arr):
	arr.sort()
	n=len(arr)
	result
	for i in xrange(n):
		l=i+1
		r=n-1
		while l<r:
			if arr[i]+arr[l]+arr[r]==0:
				result.append((arr[i],arr[l],arr[r]))
				l+=1
				r-=1
			elif arr[i]+arr[l]+arr[r]<0:l+=1
		else: r-=1

#First negative integer in every window of size k

#Given an array and a number x check for a pair with sum as x
def f(arr, x, n=len(arr)):
	l,h=0,n-1
	arr.sort()
	while l<h:
		if arr[l]+arr[h]==x: return (l,h)
		if arr[l]+arr[h]<x:l+=1
		else: h-=1
	return (-1,-1)

#find the pair in array whose sum is closest to x
def f(arr,x,n=len(arr)):
	arr.sort()
	l,h=0,n-1
	diff=99999999
	while l<h:
		if arr[l]+arr[h]-x<diff: diff=arr[l]+arr[h]-x
		elif arr[l]+arr[h]<x:l+=1
		else: h-=1

#Find the closest pair from two sorted arrays
def f(a1,a2,x,n=len(arr)):
	arr.sort()
	m,n,l,h=len(a1),len(a2),0,len(a2)-1
	diff=999999999
	while l<m and n>=0:
		if diff<a1[l]+a2[h]-x: diff=a1[l]+a2[h]-x
		elif a1[l]+a2[h]<x: l+=1
		else: h-=1

================================================================================================================================

#2 sum
def f(arr, x, n=len(arr)):
	l,h=0,n-1
	arr.sort()
	while l<h:
		if arr[l]+arr[h]==x: return (l,h)
		if arr[l]+arr[h]<x:l+=1
		else: h-=1
	return (-1,-1)

#3 sum
def f(arr,x):
	arr.sort()
	n=len(arr)
	result
	for i in xrange(n):
		l=i+1
		r=n-1
		while l<r:
			if arr[i]+arr[l]+arr[r]==x:
				result.append((arr[i],arr[l],arr[r]))
				l+=1
				r-=1
			elif arr[i]+arr[l]+arr[r]<x:l+=1
		else: r-=1

#4 sum
#sort and then keeping (0..n-3) use 3 sum





