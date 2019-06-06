class Node:
	def __init__(self, data):
		self.data=data
		self.left=None
		self.right=None

def height(node):
	if node==None: return 0
	return max(height(node.left), height(node.right))+1

def depth(node,d=0):
	if node==None: return
	depth(node.left,d+1)
	depth(node.right,d+1)

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

#using stack
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

def levelorder(root):
	queue=[]
	queue.append(root)
	while queue:
		for _ in xrange(size(queue)):
			node=queue.pop(0)
			print node.data
			if node.left:queue.append(node.left)
			if node.right:queue.append(node.right)
		print '\n'

#If 2 Tree Nodes shares the same vertical level then the one with lesser depth will come first. Level order traversing.
def vertical_order_traversal(node):
	if A is None: return []
	q=[]
    q.append((0,A))
    d=defaultdict(list)
    while q:
        l=len(q)
        for _ in xrange(l):
            node=q.pop(0)
            d[node[0]].append(node[1].val)
            if node[1].left is not None: q.append((node[0]-1,node[1].left))
            if node[1].right is not None: q.append((node[0]+1,node[1].right))
    result=[]
    for i in sorted(d.keys()):
        result.append(d[i])
    return result

#bottom view is created by vertical order traveral
def bottom_view(node):
	queue=[]
	queue.append(node)
	result={}
	mapping={}
	mapping[node]=0
	while queue:
		l=len(queue)
		for _ in xrange(l):
			poped=queue.pop(0)
			result[mapping[poped]]=poped.val
			if poped.left: 
				queue.append(poped.left)
				mapping[poped.left]=mapping[poped]-1
			if poped.right:
				queue.append(poped.right)
				mapping[poped.right]=mapping[poped]+1

#level order traversal in spiral form
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

#left view of binary tree
def left_view(node):
	queue=[]
	while queue:
		l=len(queue)
		print queue[0]
		for i in xrange(l):
			node=q.pop(0)
			if node.left: queue.append(node.left)
			if node.right: queue.append(node.right)

def lca(node,lca=None, n1, n2):
	if node==None: return False
	left,right=self.lca(node.left),self.lca(node.right)
	if ((left and right) or ((node.data==n1 or node.data==n2) and (left or right))): lca = node.data
	return left or right

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

def max_sum_of_nodes_no_two_are_adjacent(node):
	global maxx
	if node==None: return 0
	left,right=max_sum_of_nodes_no_two_are_adjacent(node.left),max_sum_of_nodes_no_two_are_adjacent(node.right)
	return max(left+right, node.data)

def invert(node):
	if node==None: return
	left=invert(node.left)
	right=invert(node.right)
	node.left=right
	node.right=left
	return node

#flatten binary tree to single linked list
	
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

#flatten binary tree to double linked list. This can also be used in questions where it is required to 
#do some operations on the bt without using extra space. Flatten it then do operations on dll
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


#check if bst. Inorder travesral of the tree like swapped two nodes question keep a pointer at the prev node
#if the previous node is bigger than the current node then the tree is not bst
def is_bst(node):
	if node.left: is_bst(node.left)
	if prev:
		if prev.val>node.val: print "not bst"
	prev=node
	if node.right: is_bst(node.right)



#Print the nodes of binary tree as they become the leaf node
#Keep a hashmap and then put(height, node.val).Calculate the height of each node order=max(left, right)
def print_nodes_bt_as_they_become_leaf_node(node,map=defaultdict(list)):
	if node==None: return 0
	order=max(ordered(node.left), ordered(node.right))+1
	map[order].append(node.val)
	return order

#check if a binary tree is a subset of another binary tree for every node check if the subtree are equal
def is_subset_tree(node, subset_node, subset_root):
	

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
	
#given a tree find distance between 2 nodes. Find the LCA of both the nodes and then use 
#distance(root,node1)+distance(root,node2)-2LCA









