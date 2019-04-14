#Find next greater element for each array element 
def next_larger_element(arr):
	stak=[]
	result=[]
	for i in xrange(len(arr)-1,-1,-1):
		while stak[len(stak)-1]<arr[i]:
			stak.pop()
		result[i] = stak[len(stak)-1] if stak else -1
		stak.append(arr[i])

#queue using 2 stacks
#making dequeue expensive



#stack using 2 queues
#making dequeue expensive



#Implement a Stack in which you can get min element in O(1) time and O(1) space.
