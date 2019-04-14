#Tim sort
#https://medium.com/@george.seif94/this-is-the-fastest-sorting-algorithm-ever-b5cee86b559c
#insertion sort (pick up an element arr[i] and insert it in a sorted sequence arr[i-1])
def insertion_sort(arr):
	for i in xrange(1,len(arr)):
		key=arr[i]
		j=i-1
		while j>=0 and key<arr[j]:
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=key

#merge sort



#quick sort


