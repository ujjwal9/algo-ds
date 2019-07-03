#Calculate the maximum sum of ‘k’ consecutive elements in the array.
#problems are solved using deque double ended queue or a heap

#https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
#maximum of all subarrays of size k.
#deque the front element is the largest
from collections import deque
q=deque()
for i in range(k):
	while q and arr[i]<arr[q[-1]]: q.pop()
	q.append(i)
for i in range(k,len(arr)):
	print arr[q[0]]
	while q and q[0]<i-k: q.popleft()
	while q and arr[q[-1]]<=arr[i]: q.pop()
	q.append(i)
print arr[q[0]]





