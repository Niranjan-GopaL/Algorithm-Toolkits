from collections import defaultdict
from math import inf
from heapq import heappop, heappush


class LinkStateAlgorithm:
    def __init__(self):
        self.topology = defaultdict(dict)

    def build_topology(self, file_name):

        with open(file_name, "r") as file:
            for line in file:
                nodes = line.strip().split()
                src, dest, cost = nodes[0], nodes[1], int(nodes[2])
                self.add_link(src, dest, cost)
                self.add_link(dest, src, cost)


    def add_link(self, src, dest, cost):
        self.topology[src][dest] = cost


    def calculate_shortest_path(self, src, dest): 
        ''' Shortest path is found using traditional Dijkstra's algorithm '''


        dist = {node: inf for node in self.topology}
        prev = {node: None for node in self.topology}

        dist[src] = 0

        pq = [(0, src)]  

        while pq:
            current_dist, current_node = heappop(pq)

            if current_node == dest: break

            if current_dist > dist[current_node]:continue

            for neighbor, cost in self.topology[current_node].items():

                new_dist = current_dist + cost

                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    prev[neighbor] = current_node

                    heappush(pq, (new_dist, neighbor))

        path = []
        current = dest
        while current:
            path.insert(0, current)
            current = prev[current]

        if dist[dest] != inf:
            print("Shortest path:", " -> ".join(path))
            print("Total cost:", dist[dest])
        else:
            print("No path found.")



print("--------------------  Link state algorithm ----------------------\n\n")  

network_topology = LinkStateAlgorithm()
network_topology.build_topology("./test_linkstate.txt")  
network_topology.calculate_shortest_path("A", "I")  

print("\n\n----------------------  END OF PROGRAM  --------------------------\n")  