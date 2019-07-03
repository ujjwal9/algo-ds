#binary search
def binary_search(arr,l,h,n):
	if h>=l:
		mid=(l+h)/2
		if mid==n: print mid
		binary_search(arr,l,mid-1,n) if n<arr[mid] else binary_search(arr,mid+1,h,n)

#Given a sorted and rotated array find a given element using binary search approach. If there are duplicates given then it will take O(n)
def f(arr,l,h,key):
	if l>h: return -1
	if arr[mid]==key: return mid
	if arr[l]<=arr[mid]:
		if key>=arr[l] and key<=arr[mid]: f(arr,l,mid-1,key)
		else: f(arr,mid+1,h,key)
	else:
		if key>=arr[mid] and key<=arr[h]: f(arr,mid+1,h,key)
		else: f(arr,l,mid-1,key)

#Given a rotated sorted array get the original array
def rverseArray(arr, start, end): 
    while (start < end): 
        temp = arr[start] 
        arr[start] = arr[end] 
        arr[end] = temp 
        start += 1
        end = end-1
  
def leftRotate(arr, d): 
    n = len(arr) 
    rverseArray(arr, 0, d-1) 
    rverseArray(arr, d, n-1) 
    rverseArray(arr, 0, n-1)


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