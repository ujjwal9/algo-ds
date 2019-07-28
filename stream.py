#Find position of an element in a sorted array of infinite numbers
def find_position(arr,n):
	l,h,val=0,1,arr[0]
	while val<n:
		l=h
		h=2*h
		val=arr[h]
	binary_search(arr,l,h,n)


#a long stream of number find the first and the last index of a number
