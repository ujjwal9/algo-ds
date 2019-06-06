#Find next greater element for each array element 
def next_larger_element(arr):
	stak=[]
	result=[]
	for i in xrange(len(arr)-1,-1,-1):
		while stak[len(stak)-1]<arr[i]: stak.pop()
		result[i] = stak[len(stak)-1] if stak else -1
		stak.append(arr[i])

#queue using 2 stacks
#making dequeue expensive



#stack using 2 queues
#making dequeue expensive



#Implement a Stack in which you can get min element in O(1) time and O(1) space.



#stock span problem. Same as previous greater element simple stack question
def stock_span(prices):
	bigger_price=[]
	result=[1 for i in xrange(len(prices))]
	bigger_price.append(prices[0])
	for i in xrange(len(prices)):
		while bigger_price and price[bigger_price[-1]]<=price[i]: bigger_price.pop()
		result[i]=i-bigger_price[-1] if bigger_price else: i+1
		bigger_price.append(i)

#trapping rain water
#largest rectangular area in a histogram

