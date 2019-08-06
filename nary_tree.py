#LCA of a n-ary tree
def lca(node,n1,n2):
	if node is None: return None
	c1,c2=None,None
	for child in node.children:
		l=lca(child,n1,n2)
		if l is not None:
			if c1 is None: c1=l
			else: c2=l
	if (c1 and c2) or ((c1 or c2) and (node.val==n1 or node.val==n2)): return node
	if node.val==n1 or node.val==n2: return node
	return c1 or c2

#minimum no of iterations to pass information to all the nodes of a tree
#all children calculate total no of pass
def f(node):
	if len(node.children)==0: return 0
	max_height=0
	height=[]
	for n in node.children: height.append(f(n)+1)
	height.sort(reversed=True)
	i=0
	for h in height:
		max_height=max(max_height,h+i)
		i+=1
	return max_height
