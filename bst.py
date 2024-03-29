#bst main property is that the inorder traversal will give you a sorted array.
class Node:
	def __init__(self, val):
		self.left=None
		self.right=None
		self.val=val

def search(node, val):
	if node==None: return False
	if val==node.val: return True
	if val>node.val: return search(node.right, val)
	return search(node.left, val)

#insertion is always done at leaf
def insert(node, new_node):
	if new_node.val>node.val:
		if node.left==None and node.right==None: node.right=new_node	
		else: insert(node.right, new_node)
	if new_node.val<node.val:
		if node.left==None and node.right==None: node.left=new_node
		else: insert(node.left, new_node)

#delete a node 
def delete(node, v):
  if node is None: return None
  if node.left in None and node.right is None and node.val==v: return None
  if node.left is None and node.right is not None and node.val==v: return node.right
  if node.right is None and node.left is not None and node.val==v: return node.left
  if node.right is not None and node.left is not None and node.val==v:
    new_node=smallest_node_in_right_side_tree(node.right)
    new_node.left=node.left
    new_node.right=node.right
    return new_node
  node.left=delete(node.left,v)
  node.right=delete(node.right,v)
  return node

#is bst. Inorder traversal should be sorted
def isBst(node):
  global prev,result
  if node.left: isBst(node.left)
  if prev and prev.val>=node.val: result=False
  else: result=result and True
  prev=node
  if node.right: isBst(node.right)

#bst two nodes are swapped recover bst. Inorder traversal gives the correct order of the elements
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

#check if a triplet with given sum exists

#Given 2 BST find an element from both such that their sum is N
#Do inorder traversal of the two bst get the array and then using two pointer find the sum  


#Convert Sorted Array to Binary Search Tree
def divide(arr, s=0, e=len(arr)):
  global root
  if s<e:
    mid=(s+e)/2
    bst(root,TreeNode(arr[mid]))
    divide(arr,s,mid)
    divide(arr,mid+1,e)
        
def bst(parent, node):
  global root
  if root is None:
    root=node
    return
  if node.val<parent.val:
    if parent.left is None: parent.left=node
    else: bst(parent.left, node)
  else: 
    if parent.right is None: parent.right=node
  else: bst(parent.right, node)

#Do a inorder and sum 
class Solution(object):
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans

#unique bst from of an arrary from 1..n 1 2 3 4 5  
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

