#disjoint data structure
#https://www.geeksforgeeks.org/union-find/
#union-find algorithm to detect cycle in a undirected graph. Self loop is not handled
from collections import defaultdict

def union(x,y):
	global parent
	xset,yset=find_parent(x),find_parent(y)
	if xset != yset: parent[xset]=yset

def find_parent(i):
	global parent
	if parent[i]==-1: return i
	find_parent(parent[i])

graph=defaultdict(list)
parent=[-1]*nodes
for i in graph:
	for j in graph[i]:
		x,y=find_parent(i),find_parent(j)
		if x==y: return True
		union(x,y)

######################################################################################

