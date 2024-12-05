class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph = {}

    def addVertex(self, vertex):
        if(not self.directed):
            self.graph[vertex] = []
        else:
            self.graph[vertex] = {
                "in": [],
                "out": []
            }

    def getVertex(self, vertex):
        return self.graph[vertex] if self.hasVertex(vertex) else None

    def hasVertex(self, vertex):
        return vertex in self.graph.keys()

    def addEdge(self, v1, v2):
        if(not self.hasVertex(v1)):
            self.addVertex(v1)
        if(not self.hasVertex(v2)):
            self.addVertex(v2)
        if(not self.directed):
            self.graph[v1].append[v2]
            self.graph[v2].append[v1]
        else:
            self.graph[v1]["out"].append(v2)
            self.graph[v2]["in"].append(v1)

    def hasEdge(self, v1, v2):
        if(not self.hasVertex(v1) or not self.hasVertex(v2)):
            return False
        if(not self.directed):
            return v2 in self.graph[v1]
        else:
            return v2 in self.graph[v1]["out"]

    def print(self):
        for key, items in self.graph.items():
            print(key, items)
# TODO: Generalize topological sort and bfs

# def bfs(vertices, node):
#     reachable = set()
#     queue = [node]
#     while len(queue) > 0:
#         vertex = queue[0]
#         queue = queue[1:]
#         if(vertex in reachable):
#             continue
#         reachable.add(vertex)
#         for outgoing in vertices[vertex]["out"]:
#             queue.append(outgoing)
#     return reachable
