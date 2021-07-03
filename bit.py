#http://graphics.stanford.edu/~seander/bithacks.html
#https://leetcode.com/discuss/general-discussion/1073221/All-about-Bitwise-Operations-Beginner-Intermediate
#https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently
#bitset: DS that can replace boolean array of visited as it uses only 1 bit 

#if a number is a power of 2
n&(n-1) == 0 ?

#number of 1s in binary representation of a number
count_one(int n):
    while(n) {
        n = n&(n-1)
        count+=1
    }
    return count

#all subsets of a given set
for i in range(0,(2**n)):# loop from 0 to (2^n)-1
    for j in range(0,n):
        if((1<<j) & i >0): #Checking if jth bit in i is set
            cursub+=(str(j+1)+" ")   
    print (cursub)
print ("All ", (2**n)," Subsets printed")

#xor swap algo
#a, b --> integers to be swapped
a = a^b   # Now a contains a^b
b = a^b   # Now b will have a
a = a^b   # Now a will have b


#XOR queries: https://leetcode.com/problems/xor-queries-of-a-subarray/
def xorQueries(self, arr: List[int], q: List[List[int]]) -> List[int]:
    l=len(arr)
    d,r=[None]*l, []
    d[0]=arr[0]
    for i in range(1,l): d[i]=arr[i]^d[i-1]
    for i in q:
        if i[0]==0: r.append(d[i[1]])
        else: r.append(d[i[1]]^d[i[0]-1])
    return r