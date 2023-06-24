from collections import defaultdict as Z
from collections import deque


class Graph:

    def __init__(self,num_of_nodes,num_of_edges,type):
        self.n = num_of_nodes
        self.m = num_of_edges
        self.type = type
        self.hashmap = Z(list)
        self.hashmap_into = Z(list)
        self.hashmap_out_off = Z(list)
        self.adjacencyList = []
        self.adjacencyMatrix = []
        self.edgeList = []

        self.initialize()



    def initialize(self):
        if self.type == "undirected":
            for i in range(self.n):
                self.hashmap[i] = []

        if self.type == "directed":
            for i in range(self.n):
                self.hashmap_into[i] = []
                self.hashmap_out_off[i] = []

        # initialize Adjacency matrix and edge list using another class


    def addEdge(self,a,b):
        if self.type == "undirected":
            self.hashmap[a].append(b)
            self.hashmap[b].append(a)

        if self.type == "directed":
            self.hashmap_into[a].append(b)
            self.hashmap_out_off[b].append(a)




    def print_graph(self):

        if self.type == "undirected":
            for u,L in self.hashmap.items():
                print(f"Vertex {u} -> ", end="")
                for v in self.hashmap[u]:
                    print(f"{v} -> ", end="")
                print("")

        if self.type == "directed":
            print("Adjacency list only contains the 'into' part \n\n")
            for u in self.hashmap_into:
                print(f"Vertex {u} -> ", end="")
                for v in self.hashmap_into[u]:
                    print(f"{v} -> ", end="")
                print("")

            print("\n\nThese are the'out of' part \n\n")
            for u in self.hashmap_out_off:
                print(f"Vertex {u} ->", end="")
                for v in self.hashmap_out_off[u]:
                    print(f"{v} -> ", end="")
                print("")


    def dfs(self, start_node): 
        visited = [False] * self.n
        self._dfs(start_node, visited)

      
    def _dfs(self, node, visited):
        visited[node] = True
        print(node, end=" ")

        for neighbor in self.hashmap[node]:
            if not visited[neighbor]:
                self._dfs(neighbor, visited)


    def bfs(self, start_node):
        visited = [False] * self.n
        Q = deque([start_node])
        visited[start_node] = True

        while Q:
            node = Q.popleft()
            print(node, end=" ")

            for neighbor in self.hashmap[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    Q.append(neighbor)


def sum_of_all_degrees(graph:Graph):

    c = 0

    if graph.type == "undirected":
        for vertex,links in graph.hashmap.items():
            print(f" vertex {vertex} => {links}")
            c += len(links)
        print()
        return c

    cin = 0
    cout = 0
    if graph.type == "directed":
        for vertex,links in graph.hashmap_into.items():
            cin += len(links)

        for vertex,links in graph.hashmap_out_off.items():
            cout += len(links)

        return (cin,cout)



c = [0]*10005
edges = [[]]*10005


def dfs(node):
    mn = c[node]
    for X in edges[node]:
        mn = min(mn,dfs(X))
    return mn






    
''' PASTE THIS IN INPUT.TXT
9 14
0 1
0 3
0 2
1 2
1 3
1 4
2 3
2 7
3 7
3 8
3 6
4 6
6 8
7 8
'''

# Open the file in read mode
file = open('./../../input_texts/input.txt', 'r')

n, m = map(int, file.readline().strip().split(' '))
g = Graph(n,m,"undirected")


print(n,m)
g.print_graph()


for _ in range(m):
    a, b = map(int, file.readline().strip().split())
    print(a,b)
    g.addEdge(a,b)

g.print_graph()
  

print("DFS traversal:")
g.dfs(0)
print("\nBFS traversal:")
g.bfs(0)


file.close() 