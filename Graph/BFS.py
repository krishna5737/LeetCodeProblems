from collections import defaultdict 
class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
	
	def addEdge(self,u,v):
		self.graph[u].append(v)
	
	def BFS(self,startNode):
		queue = []
		visited_node = [False]*(len(self.graph))
		queue.append(startNode)
		visited_node[startNode] = True
		while queue:
			s = queue.pop(0)
			print(s,end=" ")
			for i in self.graph[s]:
				if(visited_node[i]==False):
					queue.append(i)
					visited_node[i] = True
			
	
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
g.BFS(2) 
