#binary search
def binary_search(arr,l,h,n):
	if h>=l:
		mid=(l+h)/2
		if mid==n: print mid
		binary_search(arr,l,mid-1,n) if n<arr[mid] else binary_search(arr,mid+1,h,n)
#Given a sorted and rotated array find a given element using binary search approach.


#Find first and last positions of an element in a sorted array
def first(arr,l,h,n):
	if l<h:
		mid=(l+h)/2
		if arr[mid]==n and (mid==0 or arr[mid-1]<n): print mid
		else first(arr,mid+1,h,n) if arr[mid]<=n else first(arr,l,mid+1,n)

def last(arr,l,h,n):
	if l<h:
		mid=(l+h)/2
		if arr[mid]==n and (mid==len(arr)-1 or arr[mid+1]>n): print mid
		else first(arr,mid+1,h,n) if arr[mid]<=n else first(arr,l,mid+1,n)