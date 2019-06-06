#Tim sort
#https://medium.com/@george.seif94/this-is-the-fastest-sorting-algorithm-ever-b5cee86b559c
#insertion sort (pick up an element arr[i] and insert it in a sorted sequence arr[i-1])
import heapq
def insertion_sort(arr):
	for i in xrange(1,len(arr)):
		key=arr[i]
		j=i-1
		while j>=0 and key<arr[j]:
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=key

#merge sort
def merge(arr,start,end):
	#half is sorted on both sides
	l=[arr[i] for i in xrange(start,(start+end)/2)]
	r=[arr[i] for i in xrange((start+end)/2),end]
	i=j=0
	k=start
	while i!=0 or j!=0:
		if l[i]<r[j]:
			arr[k]=l[i]
			i+=1
		else:
			arr[k]=r[j]
			j+=1
		k+=1

	while i<len(l)-1:
		arr[k]=l[i]
		k+=1
		i+=1

	while j<len(r)-1:
		arr[k]=r[j]
		k+=1
		i+=1

def split(arr,start,end):
	if start<end:
		split(arr,start,(start+end)/2)
		split(arr,(start+end)/2,end)
		merge(arr,start,end)

#quick sort
#make first element as pivot.Its a two pointer question.
def partition(arr,start,end):
	i=start+1
	pivot=arr[start]
	for j in xrange(start+1, end):
		if arr[j]<pivot:
			arr[i],arr[j]=arr[j],arr[i]
			i+=1
	arr[start],a[i-1]=arr[i-1],arr[start]
	return i-1
	
def quick_sort(arr,start,end):
	if start<end:
		p=partition(arr,start,end)
		quick_sort(arr,start,p-1)
		quick_sort(arr,p+1,end)



# ======================================================
# #nuts and bolts

# #merge k sorted arrays
def merge_k_sorted_arrays(arr,k):
	heap=[]
	for i in xrange(k): heapq.heappush(heap, (arr[i][0],(i,0)))
	while heap:
		popped=heapq.heappop(heap)
		if len(arr[popped[1][0]])>popped[1][1]+1:
			heapq.heappush(heap, (arr[popped[1][0]][popped[1][1]+1], (popped[1][0],popped[1][1]+1)))
		print popped[0]

#merge k sorted ll
	
===========================================================
#count number of inversions(nlogn)

============================================================
#Number of swaps to sort when only adjacent swapping allowed
#count no of inversions

==========================================================
#Minimum number of swaps required to sort an array
#sort the array and then loop over the wrong array and keep putting the value at correct position

===========================================================

#Maximum number of partitions that can be sorted individually to make sorted
def maxPartitions(arr, n): 
    ans = 0; max_so_far = 0
    for i in range(0, n):  
        max_so_far = max(max_so_far, arr[i]) 
          if (max_so_far == i): 
            ans += 1
    return ans 
 


