# your code goes here
from collections import defaultdict 
class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
	
	def addEdge(self,u,v):
		self.graph[u].append(v)
	
			
	def DFSUtils(self,v,visited_node):
		visited_node[v]=True
		print(v,end=" ")
		for i in self.graph[v]:
			if(visited_node[i]==False):
				self.DFSUtils(i,visited_node)
		
	def DFS(self,startNode):
		visited_node = [False]*(len(self.graph))
		self.DFSUtils(startNode,visited_node)
	
	
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
g.DFS(2) 
