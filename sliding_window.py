#sliding window questions store only the point of interest elements in the deque
#For eg in First negative integer in every window of size k store only the negative values and not the positive ones also

#Calculate the maximum sum of ‘k’ consecutive elements in the array.
#problems are solved using deque double ended queue or a heap

#https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
#maximum of all subarrays of size k.
#deque the front element is the largest
from collections import deque
q=deque()
for i in range(k):
	while q and arr[i]>=arr[q[-1]]: q.pop()
	q.append(i)
for i in range(k,len(arr)):
	print arr[q[0]]
	while q and q[0]<i-k: q.popleft()
	while q and arr[i]>=arr[q[-1]]: q.pop()
	q.append(i)
print arr[q[0]]


#First negative integer in every window of size k
