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

