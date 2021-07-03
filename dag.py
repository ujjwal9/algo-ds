#Topologocal sort for DAG. Linear ordering of vertices such that for every directed edge uv u comes before v in ordering
#Add vertices in DFS then reverse.
def topological_sort(node, stak=[], visited):
	visited[node]=True
	for n in graph[node]:
		if not visited[n]: topological_sort(n, stak, visited)
	stak.append(node)
reversed(stak)

#alien dictionary. Given a sorted dictionary (array of words) of an alien language, find order of characters in the language
#take 2 words and find the first not equal alphabet and add and edge to them. Topological sort it
def alien_dictionary(words):
	graph=defaultdict(list)
	for i in xrange(len(words)-1):
		j=0
		while j<min(len(words[i]), len(words[i+1])) and words[i][j]==words[i+1][j]: j+=1
		graph[words[i][j]].append(words[i+1][j])
    
	visited={}
	for node in graph.keys(): visited[node]=False
	result=[]
	for node in graph.keys():
		if visited[node]==False: topological_sort(node, visited, result)
	print result

#Given a set of packages wor jars, with dependencies over each other. Write code to provide ordering, in which these packages should be compiled.

#Generate all palindromic numbers less than n

#Leetcode. Course Schedule. Make a DAG and check if it non cyclic
from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph=self.make_graph(prerequisites)
        visited,parents=[False]*numCourses,[False]*numCourses
        for i in xrange(numCourses):
            if not visited[i] and self.is_cyclic(i, graph,visited,parents): return False
        return True
    
    def make_graph(self, p):
        graph=defaultdict(list)
        for i in p: graph[i[0]].append(i[1])
        return graph
    
    def is_cyclic(self, node, graph, parents, visited):
        visited[node],parents[node]=True,True
        for i in graph[node]:
            if parents[i]==True: return True
            if visited[i] == False:
                if self.is_cyclic(i,graph, parents, visited): return True
        parents[node]=False
        return False


#course schedule 2. https://leetcode.com/problems/course-schedule-ii/
#Make the graph. Find ifCyclic. ifCylic return [] else do a topological sort of the graph

