#Graph:
# Only difference between a tree and graph is that graphs may contain cycles also, so we can come to same node again.
#To avoid processing a node more than once, we use a boolean visited array.
from collections import defaultdict
import sys

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

	def check_cycle_undirected_graph(self):
		self.DFS(self.graph.keys()[0])
		for i in self.visited:
			if i == True: print("Non cyclic")
			else: print("cyclic")

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

g = Graph(4)
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
g.DFS(2)
g.visited = [False]*4
g.BFS(2)

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
class adj_matrix_graph():
	def __init__(self, vertices):
		self.V=vertices
		self.graph=[[0 for column in xrange(vertices)] for row in xrange(vertices)]

	def min_distance(self, dist, spt_set):
		min=sys.maxint
		for v in xrange(self.V):
			if dist[v]<min and spt_set[v]==False:
				min=dist[v]
				min_index=v
		return min_index


	def dijkstra(self, src):
		dist=[(sys.maxint)]*self.V
		dist[src]=0
		spt_set=[False]*self.V
		for _ in xrange(self.V):
			u=self.min_distance(dist, spt_set)
			spt_set[u]=True
			for v in xrange(self.V):
				if self.graph[u][v]>0 and spt_set[v]==False and dist[v]>dist[u]+self.graph[u][v]:
					dist[v]=dist[u]+self.graph[u][v]

g = adj_matrix_graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
           [0, 0, 2, 0, 0, 0, 6, 7, 0] 
          ]


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


#Word boggle
#consider every character as a starting character and find all possible words using DFS

#Topologocal sort


#Convex hull(Graham scan o(nlogn))


