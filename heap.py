#Since heap is a complete binary tree so it can be represented as an array.
#Parent node is greater or smaller than the leaf nodes => i => 2*i+1, 2*i+2 index at 0
#Build a max heap tree O(n)
#Extract max k times O(klogn+n)

def heapify(arr, n, i):
	largest=i
	if 2*i+1<n and arr[i]<arr[2*i+1]: largest=2*i+1
	if 2*i+1<n and arr[i]<arr[2*i+2]: largest=2*i+2
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

