from collections import defaultdict
N=30
moves=[-1]*N
#ladders
moves[2] = 21
moves[4] = 7
moves[10] = 25
moves[19] = 28

#snakes
moves[26] = 0
moves[20] = 8
moves[16] = 3
moves[18] = 6

graph=defaultdict(list)
#making a directed graph that is cyclic
def make_graph():
	for i in xrange(N):
		if moves[i] != -1:
			graph[i].append(moves[i])
		else:
			for j in xrange(1, 7):
				if i+j<=29: graph[i].append(i+j)

def bfs(graph):
	q=[]
	visited=[False]*N
	q.append(graph[0])
	turns = 0
	while q:
		l=len(q)
		for i in xrange(l):
			node=q.pop(0)
			if node==N-1: return turns
			for i in graph[node]:
				if !visited[node]: q.append(i)
		turns=turns+1





