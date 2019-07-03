#Topologocal sort for DAG
def topological_sort(node, stak=[], visited):
	visited[node]=True
	for n in graph[node]:
		if not visited[n]: topological_sort(n, stak, visited)
	stak.append(node)
reversed(stak)

#alien dictinoary
#take 2 words and find the first not equal alphabet and add and edge to them. Topological sort it
def alien_dictionary(words):
	graph=defaultdict(list)
	for i in xrange(len(words)-1):
		j=0
		while j<min(len(words[i]), len(words[i+1])) and words[i][j:j+1]!=words[i+1][j:j+1]: j+=1
		graph[words[i][j:j+1]].append(words[i+1][j:j+1])
	visited={}
	for node in graph.keys(): visited[node]=False
	result=[]
	for node in graph.keys():
		if visited[node]==False: topological_sort(node, visited, result)
	print result


#Given a set of packages or jars, with dependencies over each other. Write code to provide ordering, in which these packages should be compiled.

#Generate all palindromic numbers less than n
