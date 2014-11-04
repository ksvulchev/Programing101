class DirectedGraph:

	def __init__(self):

		self.graph = {}

	def addEdge(self, nodeA, nodeB):
		if nodeA not in self.graph:
			self.graph[nodeA] = [nodeB]
		else:
			self.graph[nodeA].append(nodeB)
		#print (self.graph)

	def getNeighborsFor(self, node):
		if node in self.graph:
			print (self.graph[node])
		else:
			print ("No such node")

	def pathBetween(self, nodeA, nodeB):

		parents = [nodeA]
		checked = []
		while parents:

			node = parents.pop(0)
			checked.append(node)
			if nodeB in self.graph[node]:
				return True
			else:
				for i in self.graph[node]:
					if i in self.graph and i not in checked:
						parents.append(i)
		return False
		

















'''

# nodeA follows nodeB

graph = DirectedGraph()


graph.addEdge("a","b")
graph.addEdge("a","f")
graph.addEdge("a","d")


graph.addEdge("b","a")
graph.addEdge("b","c")

graph.addEdge("f","a")
graph.addEdge("f","u")

graph.addEdge("d","z")


#graph.getNeighborsFor("a")
print (graph.pathBetween("b","z")) '''