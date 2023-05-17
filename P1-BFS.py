# Graph adjacent verteces
# 0-> 1,2
# 1-> 3
# 2-> 3,4,5
# 3-> 2
# 4->
# 5-> 4
from collections import defaultdict


class Graph:

    # constructor
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False]*(max(self.graph)+1)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            visited[s] = True

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


if __name__ == '__main__':
    g = Graph()

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 2)
    g.addEdge(5, 4)
    # Hello everyone
    print("The result of BFS Traversal (Starting from vertex 2):")
    g.BFS(2)
