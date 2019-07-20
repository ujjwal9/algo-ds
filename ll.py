#reverse a ll
def reverse(cur, prev):
	if cur.next==None:
		head=cur
		cur.next=prev
		return
	next=cur.next
	cur.next=prev
	reverse(next, cur)

## given a infinitely long ll and no head pointer and a pointer to a node that has to be deleted.
# change the value of the current node to the value of the next node and then delete the next node.

#detect loop in ll and remove it 
def f(slow,fast,parent=None):
	if slow==fast and parent is not None: parent.next=None
	if slow and fast and fast.next: f(slow.next, fast.next.next, slow)
