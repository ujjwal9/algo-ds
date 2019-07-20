def gcd(a,b):
	if b==0: return a
	return gcd(b, a%b)

def lcm(arr):
	ans=arr[0]
	for i in xrange(1,len(arr)):
		ans=(ans*arr[i])/gcd(ans,arr[i])
	return ans