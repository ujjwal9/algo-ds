#Graph:
# Only difference between a tree and graph is that graphs may contain cycles also, so we can come to same node again.
#To avoid processing a node more than once, we use a boolean visited array.
from collections import defaultdict
import sys
import heapq

#DFS connnected graph O(V+E)
#graph can be either be represented as a matrix, as a map or a node with children
#the visited array is required for a undirected tree not for a DAG like tree
class Graph:
	def __init__(self, no_of_nodes):
		self.graph = defaultdict(list)
		self.visited=[False]*no_of_nodes
		
	def addEdge(self, u, v):
		self.graph[u].append(v)

	def DFS(self, v):
		self.visited[v]=True
		print(v)
		for i in self.graph[v]: 
			if self.visited[i]==False: self.DFS(i)

	def BFS(self, v):
		self.visited[v] = True
		queue=[]
		queue.append(v)
		while queue:
			node = queue.pop(0)
			print(node)
			for i in self.graph[node]:
				if(self.visited[i] == False):
					self.visited[i] = True
					queue.append(i)

	def level_order_traversal(self, v):
		self.visited[v]=True
		queue=[]
		queue.append(v)
		while queue:
			l=size(queue)
			for _ in xrange(l):
				node=queue.pop(0)
				print(node)
				for child in self.graph[node]:
					if !self.visited[child]:
						self.visited[child]=True
						node.append(child)

	def check_cycle_undirected_graph(self, node, parent):
		visited[node]=True
		for adj in graph[node]:
			if visited[adj] and adj!=parent: return True
			if check_cycle_undirected_graph(adj, node): return True
		return False

	def check_cycle_DAG(self, node, parents):
		self.visited[node]=True
		parents[node]=True
		for i in self.graph[node]:
			if self.visited[i]==False:
				if self.check_cycle_DAG(i, parents) == True: return True
			elif parents[i]==True: return True
		parents[node]=False
		return False

	def check_if_cyclic_DAG(self):
		parents=[False]*self.no_of_nodes
		for i in self.graph:
			if visited[i]==False:
				if check_cycle_DAG(i, parents) == True: return True
		return False

	#check if a DAG is strongly connected
	def scc(graph):


	#do BFS use m=2 coloring problem and assign it to 2 coloring groups
	def is_bapartite(self, node):
		color=[-1]*self.no_of_nodes
		queue=[]
		queue.append(node)
		while queue:
			int l = queue.length
			for _ in xrange(l):
				u=queue.front()
				for v in self.graph[u]:
					if u in self.graph[u]: return False
					if color[v] == -1: 
						color[v]=1-color[u]
						queue.push(v)
					else if color[v] == color[u]: return False
		return True	

===================================================================================================================
#SPT(Shortest path tree)
#Dijskstras Greedy approach
# 1) One source and One Destination-
# → Use A* Search Algorithm (For Unweighted as well as Weighted Graphs)

# 2) One Source, All Destination –
# → Use BFS (For Unweighted Graphs)
# → Use Dijkstra (For Weighted Graphs without negative weights)
# → Use Bellman Ford (For Weighted Graphs with negative weights)

# 3) Between every pair of nodes-
# → Floyd-Warshall
#dijkstras and prims are almost same only in dijkstras sum of distance is taken

#Floyd Warshall O(v^3)
INF=9999999
vertices=4
def floyd_warshall(graph):
	dist=[row[:] for row in graph]
	for k in xrange(vertices):
		for i in xrange(vertices):
			for j in xrange(vertices):
				dist[i][j]=min(dist[i][j], dist[i][k]+dist[k][j])


graph = [[0,5,INF,10], 
         [INF,0,3,INF], 
         [INF, INF, 0,   1], 
         [INF, INF, INF, 0]]

#minimum spanning tree
#Given an undirected and connected graph , a spanning tree of the graph  is a tree that spans 
#(that is, it includes every vertex of)and is a subgraph of (every edge in the tree belongs to)
#prims mst greedy algorithm
class Node():
	def __init__(self, min_distance):
		adjacencies=[]
		min_distance=sys.MAX_INT


class Edge():
	def __init__(self, target, weight):
		self.target=target
		self.weight=weight

def prims(root):
	root.min_distance=0
	reached_nodes=[]
	node_queue=[]
	heapq.heappush(node_queue, (root.min_distance, root))
	while node_queue:
		popped=heapq.heappop(node_queue)
		reached_nodes.append(popped)
		for edge in popped.adjacencies:
			node=edge.target
			if node not in reached_nodes and node.min_distance>edge.weight:
				node.min_distance=e.weight
			node_queue.append(node)
			heapq.heapify(node_queue)

def dijkstra(root):
	root.min_distance=0
	reached_nodes=[]
	node_queue=[]
	heapq.heappush(node_queue, (root.min_distance, root))
	while node_queue:
		popped=heapq.heappop(node_queue)
		reached_nodes.append(popped)
		for e in popped.adjacencies:
			node=e.target
			new_distance=e.weight+popped.min_distance
			if node not in reached_nodes and node.min_distance>new_distance:
				node.min_distance=new_distance
			node_queue.append(node)
			heapq.heapify(node_queue)
			
def kruskal():

def bellman_ford():

===================================================================================================================
#Flood fill algorithm O(nxm)
def dfs(x,y,visited,n,m):
	if (x<0 or x>n or y<0 or y>n or visited[x][m]): return
	visited[x][y]=True
	dfs(x+1,y,visited,n,m)
	dfs(x,y+1,visited,n,m)
	dfs(x-1,y+1,visited,n,m)
	dfs(x-1,y,visited,n,m)
	dfs(x-1,y-1,visited,n,m)
	dfs(x,y-1,visited,n,m)
	dfs(x+1,y+1,visited,n,m)

===================================================================================================================
#minimize cash flow among a group of friends who owe each other money
def get_max_credit(arr):
	result=0
	for i in xrange(len(arr)):
		if arr[i]>arr[result]: result=i
	return result

def get_max_debit(arr):
	result=0
	for i in xrange(len(arr)):
		if arr[i]<arr[result]: result=i
	return result

def min_cash_flow(amount):
	max_credit=get_max_credit()
	max_debit=get_max_debit()
	if amount[max_debit]==0 and amount[max_credit]==0: return
	minn=min(-amount[max_debit],amount[max_credit])
	amount[max_credit]-=minn
	amount[max_debit]+=minn
	print("Person " , max_debit , " pays " , minn, " to Person " , max_credit) 
	min_cash_flow(amount)

# graph[i][j] indicates the amount that person i needs to pay person j 
graph = [ [0, 1000, 2000], 
          [0, 0, 5000], 
          [0, 0, 0] ] 

amount=[0 for _ in xrange(N)]
for p in xrange(N):
	for i in xrange(N): amount[p]+=(graph[i][p]-graph[p][i])

min_cash_flow(amount)

===================================================================================================================


#minimum steps to reach target by a knight. BFS


===================================================================================================================

#clone an undirected graph
def f(node,n_node,mapp):
    mapp[n_node.val]=n_node
    for n in node.neighbors:
        new_node=mapp.get(n.val, Node(n.val,[]))
        n_node.neighbors.append(new_node)
        if new_node.val not in mapp: f(n,new_node,mapp)	

f(node,Node(node.val,[]),{})

