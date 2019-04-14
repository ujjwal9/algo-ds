#Activity selection
#Given n activities with start and finish times. Select max no of activities that can be performed
def activity_selection(start, end):
	t=zip(start, end)
	sort=sorted(t, key=lambda x:x[1])
	result=1
	for i in xrange(1, len(sort)):
		if sort[i][0]>=sort[i-1][1]: result+=1
	print result