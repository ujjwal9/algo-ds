class Node:
	def __init__(self, val):
		self.left=None
		self.right=None
		self.val=val

def search(node, val):
	if node==None: return False
	if val>node.val: return self.search(node.right, val)
	if val<node.val: return self.search(node.left, val)
	return True

#insertion is always done at leaf
def insert(node, new_node):
	if node==None:return
	if new_node.val>node.val:
		if node.left==None and node.right==None:node.right=new_node	
		else: self.insert(node.right, new_node)
	if new_node.val<node.val:
		if node.left==None and node.right==None:node.left=new_node
		else:self.insert(node.left, new_node)