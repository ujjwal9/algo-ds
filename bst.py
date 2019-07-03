#bst main property is that the inorder traversal will give you a sorted array.
class Node:
	def __init__(self, val):
		self.left=None
		self.right=None
		self.val=val

def search(node, val):
	if node==None: return False
	if val==node.val: return True
	if val>node.val: return self.search(node.right, val)
	else: return self.search(node.left, val)

#insertion is always done at leaf
def insert(node, new_node):
	if new_node.val>node.val:
		if node.left==None and node.right==None:node.right=new_node	
		else: self.insert(node.right, new_node)
	if new_node.val<node.val:
		if node.left==None and node.right==None:node.left=new_node
		else:self.insert(node.left, new_node)

#bst two nodes are swapped. Inorder traversal gives the correct order of the elements
def swapped(node):
	global prev,p1,p2
  if node.left: swapped(node.left)
  if prev is not None:
    if node.val < prev.val:
      p2 = node
      if p1 is None:
        p1 = prev        
  prev = node
  if node.right: swapped(node.right)

#unique bst from of an arrary from 1..n
 def numTrees(self, n):
    dp=[0]*(n+1)
    dp[1]=1
    for i in xrange(2,n+1):
        for j in xrange(1,i+1):
            right,left=1,1
            if j-1>0: left=dp[j-1]
            if i-j>0: right=dp[i-j]
            dp[i]+=left*right
    return dp[n]

#is bst. Inorder traversal should be sorted
def isBst(node):
	global prev,result
  if node.left: isBst(node.left)
  if prev and prev.val>=node.val: result=False
  else: result=result and True
  prev=node
  if node.right: isBst(node.right)

#check if a triplet with given sum exists


  