from collections import defaultdict as Z

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




    def addEdge(self,type,a,b):
        if type == "undirected":
            self.hashmap[a].append(b)

        if type == "directed":
            self.hashmap_into[a].append(b)
            self.hashmap_out_off[b].append(a)




    def print_graph(self):
        if self.type == "undirected":
            for u in self.hashmap:
                print(f"Adjacency list of vertex {u}: ", end="")
                for v in self.graph[u]:
                    print(f"{v} -> ", end="")
                print("")


def sum_of_all_degrees(graph:Graph):

    c = 0
    if graph.type == "undirected":
        for vertex,links in graph.hashmap:
            c += len(links)
            return c

    cin = 0
    cout = 0
    if graph.type == "directed":
        for vertex,links in graph.hashmap_into:
            cin += len(links)

        for vertex,links in graph.hashmap_out_off:
            cout += len(links)

        return (cin,cout)



n,m = list(map(int,input().split()))

g = Graph(n,m,"undirected")

for _ in range(m):
    a,b = list(map(int,input().split()))
    g.addEdge(a,b)

print(f"Number of edges : {m} and Sum of all degrees : {sum_of_all_degrees(g)}  ")

# g = Graph(n,"directed")