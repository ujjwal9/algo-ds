#ll questions are combinations of reversing and fast and slow moving pointers
#ll can be merged sort
#quick sort a ll
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

#delete a node in ll
def delete(node, num):
  head = node
  if node.next is None:
    if node.val == num : return None
      return node
  prev = node
  node = node.next
  while node:
    if node.val==num:
      prev.next=node.next
      break
    prev=node
    node=node.next
  return head

#get nth element from the end of a ll. 1 calculate the length then (n-L+1). 2 recursicve.
# 3 2 pointers with L distance apart

#middle point of the linked list

#if a ll is palindrome or not
#or get the middle point and reverse the other half and then with the first and second half
#compare the values and then again reverse the second half
def f(left,right):
	if right is None: return left
	l=None
	while right is not None: l=f(left, right.next)
	if l is None or l.val!=right.val: return None
	return l.next

#intersection of point of 2 ll
#get the length of 2 ll l1 and l2. From the bigger ll reach at l1-l2. Then traverse both
#ll simultaneously till both the nodes of ll are same

#A doubly linked list having exactly one of the node pointing to a random node in list, correct the doubly linked list.
#check which pointer is longer and then check for each node

#https://www.geeksforgeeks.org/pairwise-swap-elements-of-a-given-linked-list-by-changing-links/

#duplicate a ll with next and random pointers
#Create the copy of node 1 and insert it between node 1 & node 2 in original Linked List

