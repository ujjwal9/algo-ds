#Find next greater element for each array element. NGE
def next_larger_element(arr):
	stak=[]
	result=[]
	for i in xrange(len(arr)-1,-1,-1):
		while stak[len(stak)-1]<arr[i]: stak.pop()
		result[i] = stak[len(stak)-1] if stak else -1
		stak.append(arr[i])

#queue using 2 stacks
#making dequeue expensive

#queue using 1 stack



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

#Celebrity problem. https://www.geeksforgeeks.org/the-celebrity-problem/
def celebrity_problem(n):
	stak=[]
	for i in xrange(1, n+1): stak.append(i)
	while len(stak)>1:
		p1,p2=stak.pop(),stak.pop()
		if(knows(p1,p2))stak.append(p2)
		elif(!knows(p1,p2))stak.append(p1)

#water drop problem. https://www.geeksforgeeks.org/water-drop-problem/. Same like stock span find local minima
def f(length,position,speed):
	drops=zip(position,speed)
	sort(drops, lambda:x x[0])
	#pop till the speed is lower than the last drop

#check for balanced paranthesis




#Design a stack such that it provides push(), pop() and min( ) is in O(1)Use only Stack not any other Data structure
class New_stack(object):
	def __init__(self):
		self.stak = []
		self.minn = []

	def append(val):
		self.stak.append(val)
		if minn[len(minn)-1]>val: minn.append(val)
		else: minn.append(minn[len(minn-1)])

	def popped():
		self.minn.pop()
		return self.stak.pop()

	def getMin():
		return self.minn[len(minn)-1]
		
