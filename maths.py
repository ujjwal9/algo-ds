def gcd(a,b):
	if b==0: return a
	return gcd(b, a%b)

def lcm(arr):
	ans=arr[0]
	for i in xrange(1,len(arr)):
		ans=(ans*arr[i])/gcd(ans,arr[i])
	return ans

#sum of all prime factors. Also https://leetcode.com/problems/2-keys-keyboard/
def minSteps(self, n: int) -> int: 
	r,d=0,2
    while n>1:
        while n%d==0:
            r+=d
            n/=d
        d+=1
    return r