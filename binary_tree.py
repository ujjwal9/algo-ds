class Node:
	def __init__(self, data):
		self.data=data
		self.left=None
		self.right=None

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
	while stack or node is not None:
		if node is not None:
			stack.append(node)
			node=node.left
		else:
			node=stack.pop()
			print node.val
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

def max_path_sum(node):
	global max_path_sum
	if node==None: return 0
	left=self.max_path_sum(node.left)
	right=self.max_path_sum(node.right)
	max_path_sum=max(left+right+node.data, node.data, node.data+left, node.data+right, max_path_sum)
	return max(node.data, node.data+left, node.data+right)

def max_path_sum_leaf_to_leaf(node):
	global max_path_sum
	if node==None: return 0
	left=self.max_path_sum_leaf_to_leaf(node.left)
	right=self.max_path_sum_leaf_to_leaf(node.right)
	max_path_sum=max(max_path_sum, left+right+node.data)
	return max(max(left, right)+ node.data)

def max_sum_of_nodes_no_two_are_adjacent(node):
	global maxx
	if node==None: return 0
	left=self.max_sum_of_nodes_no_two_are_adjacent(node.left)
	right=self.max_sum_of_nodes_no_two_are_adjacent(node.right)
	return max(left+right, node.data)

def lca(node,lca=None, n1, n2):
	if node==None: return False
	if (self.lca(node.left) and self.lca(node.right) or node.data==n1 or node.data==n2):
		lca = node.data
		return True
	return left or right

def invert(node):
	if node==None: return
	left=invert(node.left)
	right=invert(node.right)
	node.left=right
	node.right=left
	return node

#flatten binary tree to single linked list
def last_right(node):
	if node.left==None and node.right==None: return node
	return last_right(node.right)
	
def bt_sll(node):
	if node==None: return
	left=bt_sll(node.left)
	right=bt_sll(node.right)
	if left is not None:
		node.right=left
		last_right(left).right=right
		node.left=None
	return node

#flatten binary tree to double linked list
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

#check if bst

#bottom view
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

#Print the nodes of binary tree as they become the leaf node


#check if a binary tree is a subset of another binary tree
def is_subset_tree(node, subset_node, subset_root):
	if node==None or subset_node==None: return True
	if node.val!=subset_node.val: 
		if node.val==subset_root.val: 
			return node.val==subset_node.val and 
			 is_subset_tree(node.left, subset_root.left, subset_root) and 
			 is_subset_tree(node.right,subset_root.right,subset_root)
		else: 
			return node.val==subset_node.val and 
		 	 is_subset_tree(node.left, subset_root, subset_root) and 
		 	 is_subset_tree(node.right,subset_root,subset_root)
	else:
		left=is_subset_tree(node.left,subset_node.left,subset_root)
		right=is_subset_tree(node.right,subset_node.right,subset_root)
		if left and right and subset_root==subset_node: print "subset exists"
		return left and right

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
	
#given a tree find distance between 2 nodes







