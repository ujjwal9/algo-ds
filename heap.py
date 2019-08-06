#Since heap is a complete binary tree so it can be represented as an array.
#Parent node is greater or smaller than the leaf nodes => i => 2*i+1, 2*i+2 index at 0
#Build a max heap tree O(n)
#Extract max k times O(klogn+n)
#https://www.geeksforgeeks.org/heap-data-structure/
#heap.heapify() for min heap and heap._heapify_max() for max heap

from heapq import heappush, heappop

#max heap
def heapify(arr, n, i):
	largest=i
	if 2*i+1<n and arr[i]<arr[2*i+1]: largest=2*i+1
	if 2*i+2<n and arr[largest]<arr[2*i+2]: largest=2*i+2
	if largest!=i:
		arr[i],arr[largest]=arr[largest],arr[i]
		heapify(arr,n,largest)

def heapsort(arr):
	n=len(arr)
	for i in xrange(n/2-1, -1, -1):
		heapify(arr, n, i)

	#extract elements one by one
	for i in xrange(n-1, -1, -1):
		arr[i],arr[0]=arr[0],arr[i]
		heapify(arr, i, 0)

#find k nearest element in an array

#sort a k sorted array
def k_sorted_array(arr,k):
	heap=arr[:k+1]
	heapify(heap)
	index=0
	for i in xrange(k+1: len(arr)):
		arr[index]=heappop(heap)
		heappush(heap,arr[i])
		index+=1
	while heap:
		arr[index]=heappop(heap)
		index+=1


#median in a stream of integers
def add(num):
	heapq.heappush(max_heap, -heapq.heappushpop(min_heap, num))
	if len(min_heap)<len(max_heap): heapq.heappush(min_heap, -heapq.heappop(max_heap))

def get_median():
	if len(min_heap)>len(max_heap): return min_heap[0]
	else: return (min_heap[0]+max_heap[0])/2

max_heap=[]
min_heap=[]
#kth largest or smallest element in heap

#merge k sorted arrays
def f(arr, k):
	h=[]
	result=[]
	for i in xrange(arr): heappush(heap,(arr[i][0],(i,0)))
	while h:
		i,j=heappop(h)
		result.append(arr[i][j])
		if j<len(arr[i]): heappush(heap,(arr[i][j+1],(i,j+1)))
	
#skyline problem
#use o(n2)

#k pairs with smallest sum. Use a min heap and add (i+1,j) and (i,j+1) and keep a set to
# check if the numbers are not duplicated in the heap



