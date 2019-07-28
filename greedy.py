#Activity selection
#Given n activities with start and finish times. Select max no of activities that can be performed.
#First activity is always selected
def activity_selection(start, end):
	t=zip(start, end)
	sort=sorted(t, key=lambda x:x[1])
	result=1
	prev=arr[0]
	for i in xrange(1, len(sort)):
		curr=arr[i]
		if curr[0]>=prev[1]:
			result+=1
			prev=curr
	print result

#merge overlapping intervals
def merge(start,end):
    zipped=zip(start,end)
    zipped=sorted(zipped, lambda x: (x[0],x[1]))
    if len(zipped) <=1: return zipped
    for i in xrange(1,len(zipped)):
     	if zipped[i][0]<=zipped[i-1][1]:
            zipped[i-1][1] = zipped[i][1]
            zipped.remove(i)
    return zipped

=========================================================================================================

#Stock Buy Sell to Maximize Profit
def maxProfit(self, prices):
	n=len(prices)
    if n<2: return 0
    greater=[0]*(n)
    for i in xrange(n-2,-1,-1):
    	if prices[i+1]>greater[i+1]: greater[i]=prices[i+1]
        else: greater[i]=greater[i+1]
    result=0
    for i in xrange(n-1):
        result=max(result,greater[i]-prices[i])
    return result 

#Stock Buy Sell to Maximize Profit
#find the local minima and local maxima and substract it and do for remaining array
def calculateProfit(buy,sell):
      if len(sell)==0: return 0
      result=0
      for i in xrange(len(sell)): result+=sell[i]-buy[i]
      return result
    
def maxProfit(prices):
    i,buy,sell,n=0,[],[],len(prices)
    while i<n:
    	while i<n-1 and prices[i+1]<prices[i]:i+=1
        if i>=n-1: return calculateProfit(buy,sell)
        buy.append(prices[i])
        while i<n-1 and prices[i+1]>=prices[i]:i+=1
        sell.append(prices[i])
    return calculateProfit(buy,sell)

=========================================================================================================

#gas station
def f(l):
	start,gas,total_gas=0,0,0
	for i in xrange(len(l)):
		pump=l[i]
		gas = gas+pump[0]
		total_gas+=pump[0]
		if gas-pump[1]<0:
			gas=0
			start=i+1
	if total_gas





