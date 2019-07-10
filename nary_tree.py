#Minimum no. of iterations to pass information to all nodes in the tree
#For each node find out the max of height and the width and return it

#LCA of a n-ary tree
def lca(node,n1,n2):
	if node is None: return None
	left,right=None,None
	for child in node.children:
		l=lca(child,n1,n2)
		if l is not None:
			if left is None: left=l
			else right=l
	if (left and right) or ((left or right) and (node.val==n1 or node.val==n2)): return node
	if node.val==n1 or node.val==n2: return node
	return left or right
