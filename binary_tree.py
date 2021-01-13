#Traversals, Construction and conversion, checking and printing, summation, LCA, misc
#ATTRIBUTES : height, Depth, Diameter
#TRAVERSAL : Preorder/Iterative, Inorder/Iterative, Postorder/Iterative, Levelorder, Verticalorder, Spiral, Diagonal, Boundary 
#VIEW : Left view, Right view, Bottom view
#LCA, Distance between 2 nodes,
#Convert to ll, dll
class Node:
	def __init__(self, data):
		self.data=data
		self.left=None
		self.right=None

===================================================================================================================
#think like a tree. Distance from the farthest leaf node to the node. Root height=maxedges
def height(node):
	if node==None: return 0
	return max(height(node.left), height(node.right))+1

#Think like a tree. Distance of the node from the root. Root depth=0
depth(node)=height(root)-height(node)

#diameter or the width of a tree is the number of nodes on the longest path between two end nodes
def diameter(node):
	global result
	if node is None: return 0
	left,right=diameter(node.left),diameter(node.right)
	result=max(result,1+left+right)
	return max(left,right)+1

===================================================================================================================

def preorder(node):
	if node=None: return
	print node.data
	preorder(node.left)
	preorder(node.right)

def inorder(node):
	if node=None: return
	inorder(node.left)
	print node.data
	inorder(node.right)

def postorder(node):
	if node==None: return
	postorder(node.left)
	postorder(node.right)
	print node.data

def level_order(root):
	queue=[]
	queue.append(root)
	while queue:
		for _ in xrange(size(queue)):
			node=queue.pop(0)
			print node.data
			if node.left:queue.append(node.left)
			if node.right:queue.append(node.right)
		print '\n'

def vertical_order_traversal(node,p=0,d=defaultdict(list)):
	if node is None: return
	d[p].append(node)
	vertical_order_traversal(node.left,p-1,d)
	vertical_order_traversal(node.right,p+1,d)

def level_order_spiral(node):
	queue=[]
	eo=1
	while queue:
		l=len(queue)
		lis=[]
		for i in xrange(l):
			node=q.pop(0)
			if node.left: queue.append(node.left)
			if node.right: queue.append(node.right)
			lis.append(node)
		if eo % 2 == 0: print reversed(lis)
		else print lis
		eo+=1

def diagonal_traversal(node,index=0,map=defaultdict(list)):
	if not node: return
	map[index].append(node.val)
	diagonal_traversal(node.left,index+1,map)
	diagonal_traversal(node.right,index,map)

===================================================================================================================

#iterative way of binary tree traversal, using stack.
def preorder_without_recursion(root):
	stack=[]
	stack.append(root)
	while stack:
		node=stack.pop()
		print node.val()
		if node.right: stack.append(node.right)
		if node.left: stack.append(node.left)

def postorder_without_recursion(root):
	stack=[]
	stack.append(root)
	result=[]
	while stack:
		node=stack.pop()
		result.append(node)
		if node.left: stack.append(node.left)
		if node.right: stack.append(node.right)
	return reversed(result)

#different than preorder and inorder
def inorder_without_recursion(root):
	stack=[]
	node=root
	while stack or node :
		if node:
			stack.append(node)
			node=node.left
		else:
			node=stack.pop()
			if node: print node.val
			node=node.right

===================================================================================================================

#boundary traversal of a binary tree
#left boundary - leaf node + all leaf node + (right boundary - leaf)
def left(node):
	if node is None or (node.left is None and node.right is None): return
	print node.val
	left(node.left)

def leaf(node):
	if node is None: return
	if node.left is None and node.right is None: print node.val
	leaf(node.left)
	leaf(node.right)

def right(node):
	if node is None or (node.left is None and node.right is None): return
	print node.val
	right(node.right)

#bottom view is created by vertical order traveral

#left view of binary tree. Level order traversal. Get the first element

#right view of binary tree. Level order traversal. Get the last element

#Populating Next Right Pointers in Each Node
def connect(self, root):
	queue=[]
	queue.append(root)
	while queue:
		l=len(queue)
        stak=[]
		for i in xrange(l):
			popped=queue.pop(0)
			stak.append(popped)
			if popped.left: queue.append(popped.left)
			if popped.right: queue.append(popped.right)
			for i in xrange(len(stak)-1):stak[i].next=stak[i+1]

===================================================================================================================

def lca(root, p, q):
	if root is None: return None
	if root.val==p.val or root.val==q.val: return root
    left,right=lca(root.left,p,q),lca(root.right,p,q)
    if right and left : return root
    return right or left

#given a tree find distance between 2 nodes. Find the LCA of both the nodes and then use 
#distance(root,node1)+distance(root,node2)-2LCA

===================================================================================================================

#four possibilities of sum at a node
def max_path_sum(node):
	global max_path_sum
	if node==None: return 0
	left,right=max_path_sum(node.left),max_path_sum(node.right)
	max_path_sum=max(left+right+node.data, node.data, node.data+left, node.data+right, max_path_sum)
	return max(node.data, node.data+left, node.data+right)

def max_path_sum_leaf_to_leaf(node):
	global max_path_sum
	if node==None: return 0
	left,right=max_path_sum_leaf_to_leaf(node.left),max_path_sum_leaf_to_leaf(node.right)
	max_path_sum=max(max_path_sum, left+right+node.data)
	return max(max(left, right)+ node.data)

#for positive no only
def max_sum_of_nodes_no_two_are_adjacent(node):
	if node==None: return 0
	left,right=max_sum_of_nodes_no_two_are_adjacent(node.left),max_sum_of_nodes_no_two_are_adjacent(node.right)
	return max(left+right, node.data)

#path sum. Root to leaf sum equal to a number
def path_sum(node, num, s=0):
	if node is None: return False
	if node.left is None and node.right is None and s+node.val==num: return True
	return path_sum(node.left, num, s+node.val) or path_sum(node.right, num, s+node.val)

#path sum2. Return all possible root to leaf paths where sum==num
def path_sum_2(node, num, s=0, l):
	global result
	if node is None: return
	total_sum=s+node.val
	l=l.append(node.val)
	if node.left is None and node.right is None and total_sum==num: result.append(l.copy())
	path_sum_2(node.left, num, total_sum, l)
	path_sum_2(node.left,num,total_sum, l)
	l.pop()

#path sum 3. Number of paths that sum to a value
def path_sum_3(node, num):
	global result,s
    if node is None: return 
    if sum-node.val in s: result+=1
    if node.val==sum: result+=1
    temp=[]
    for n in s: temp.append(n+node.val)
    temp.append(node.val)
    s=temp
    temp=[]
    t(node.left, sum)
    t(node.right, sum)
    s.remove(node.val)
    for n in s: temp.append(n-node.val)
    s=temp

result=0
s=[]
path_sum_3(node, num)


result=0
s=set()

#find sum of only left nodes
def f(node):
	if node is None: return
	if node.left: sum+=node.left.val
	f(node.left)
	f(node.right)

result=0
===================================================================================================================

def invert(node):
	if node==None: return
	left, right=invert(node.left), invert(node.right)
	node.left, node.right=right, left
	return node

===================================================================================================================

#flatten binary tree to linked list	
def bt_sll(node):
	if node==None: return
	left=bt_sll(node.left)
	right=bt_sll(node.right)
	if left is not None:
		node.right=left
		while(left.right!=None): left=left.right
		left.right=right
		node.left=None
	return node

#flatten binary tree to double linked list.This is inorder formation.This can also be used in
#questions where it is required to do some operations on the bt without using extra space. Flatten it then do operations on dll
def bt_dll(node):
	global prev
	if node==None: return
	bt_dll(node.left)
	if prev==None: head=node
	else:
		node.left=prev
		prev.right=node
	prev=node
	bt_dll(node.right)

===================================================================================================================

#Print the nodes of binary tree as they become the leaf node
#Keep a hashmap and then put(height, node.val).Calculate the height of each node order=max(left, right)
def print_nodes_bt_as_they_become_leaf_node(node,map=defaultdict(list)):
	if node==None: return 0
	order=max(print_nodes_bt_as_they_become_leaf_node(node.left), print_nodes_bt_as_they_become_leaf_node(node.right))+1
	map[order].append(node.val)
	return order

===================================================================================================================

#check if a binary tree is a subset of another binary tree for every node check if the subtree are equal
def is_subset_tree(node, subset_node, subset_root):
	
===================================================================================================================
#construct a binary tree from inorder and preorder traversal
#first element of preorder is root. Find the elements in the inorder as the sequence in preorder and construct the tree

#construct a binary tree from inorder and postorder traversal


#construct a binary tree from given array in level order fashion
def construct_complete_binary_tree(arr):
	for i in xrange(len(arr)): arr[i]=Node(arr[i])
	for i in xrange(len(arr)):
		if 2*i+1<len(arr): arr[i].left=arr[2*i+1]
		if 2*i+2<len(arr): arr[i].right=arr[2*i+2]

#constrcut a binary tree from array
#https://www.geeksforgeeks.org/construct-a-binary-tree-from-parent-array-representation
def construct_binary_tree_from(arr):
	map={}
	for i in xrange(len(arr)): map[i]=Node(i)
	for i in xrange(len(arr)):
		if arr[i]==-1: head=map[i]
		else:
			parent=map[arr[i]]
			if parent.left==None: parent.left=map[i]
			else parent.right=map[i]

===================================================================================================================

def all_full_binary_tree(node):


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


===================================================================================================================
#https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
# def recoverFromPreorder(self, s):
# 	root=TreeNode(s[0])
#     parents=defaultdict(list)
#     parents[0].append(root)
#     depth=0
#     for i in xrange(1,len(s)):
# 	    if s[i] != '-':
# 	        n=TreeNode(s[i])
# 	        parent=parents[depth-1][len(parents[depth-1])-1]
# 	        if parent.left is None: parent.left=n
# 	        else: parent.right=n
# 	        parents[depth].append(n)
# 	        depth=0
# 	    else:depth+=1
#    return root

===================================================================================================================

#Two Trees are isomorphic or not
def is_isomorphic(n1,n2):
	if n1 is None and n2 is None: return True
	if n1 is None or n2 is None or n1.val != n2.val: return False
	return (is_isomorphic(n1.left,n2.left) and is_isomorphic(n1.right,n2.right)) or (is_isomorphic(n1.left,n2.right) and is_isomorphic(n1.right,n2.left))

===================================================================================================================

#Print all nodes at distance k from a given node
#Given a binary tree, a destination node and an integer value given_depth return a list of nodes at a distance of given_depth
def find_parent(node):
	if node is None: return
	if node.left:
		parent[node.left]=node
		find_parent(node.left)
	if node.right:
		parent[node.right]=node
		find_parent(node.right)=node

def dfs(target, k):
	if target==null or visited[target]==True or k<0: return
	visited[target]=True
	if k==0: result.append(target)
	dfs(target.left,k-1)
	dfs(target.right,k-1)
	dfs(parent[target], k-1)

parent={}
result=[]
visited={}


#given a binary tree how long will it take to burn the whole tree
def find_parent(node):
	if node is None: return
	if node.left:
		parent[node.left]=node
		find_parent(node.left)
	if node.right:
		parent[node.right]=node
		find_parent(node.right)=node

def dfs(target, k):
	if target==null or visited[target]==True: return
	visited[target]=True
	result=max(result,k)
	dfs(target.left,k+1)
	dfs(target.right,k+1)
	dfs(parent[target], k+1)

parent={}
result=-1
visited={}

===================================================================================================================
#serialize and deserialize a binary tree. Can be serialized like preorder keeping the null as -1 and also level order traversal
def serialize(node):
	if node is None:
		print -1
		return
	print node.val
	f(node.left)
	f(node.right)

def deserialize():
	global i, arr, root
	if i>=len(arr) or arr[i]==-1: return
	node=Node(arr[i])
	i+=1
	node.left=deserialize()
	i+=1
	node.right=deserialize()
	return node
#[8 4 -1 -1 12 10 -1 -1 14 -1 -1 -1]
===================================================================================================================
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

===================================================================================================================
#Merge Two Binary Trees
def mergeTrees(t1, t2):
	if t1 is None and t2 is None: return
    if t1 is None: return t2
    if t2 is None: return t1
    t1.val=t1.val+t2.val
    t1.left,t1.right=mergeTrees(t1.left,t2.left),mergeTrees(t1.right,t2.right)
    return t1

===================================================================================================================
#Reverse tree path using Queue
#https://www.geeksforgeeks.org/reverse-tree-path-using-queue/
from collections import deque
def f(node,n):
	if node is None: return None
	if node is n and q:
		new_node=q.popleft()
		q.add(node)
		return new_node
	q.add(node)
	node.left, node.right=f(node.left,n),f(node.right,n)

	return node




q=[]


