from queue import PriorityQueue

def shortest_longest_path_dag(graph, source):
    n = len(graph)
    shortest_dist = [float('inf')] * n
    longest_dist = [float('-inf')] * n
    shortest_dist[source] = 0
    longest_dist[source] = 0

    queue = PriorityQueue()
    queue.put((0, source))

    while not queue.empty():
        dist, u = queue.get()

        # Update shortest and longest distances for adjacent vertices
        for v, weight in graph[u]:
            new_shortest_dist = shortest_dist[u] + weight
            new_longest_dist = longest_dist[u] + weight

            if new_shortest_dist < shortest_dist[v]:
                shortest_dist[v] = new_shortest_dist
                queue.put((new_shortest_dist, v))

            if new_longest_dist > longest_dist[v]:
                longest_dist[v] = new_longest_dist
                queue.put((new_longest_dist, v))

    return shortest_dist, longest_dist




# Example graph represented as an adjacency list
graph = [
    [(1, 3), (2, 5)],         # Node 0: (to node, weight)
    [(3, 2), (4, 4)],         # Node 1
    [(1, 6), (4, 1)],         # Node 2
    [(4, 2), (5, 3)],         # Node 3
    [(5, 4)],                 # Node 4
    []                        # Node 5
]

source = 0

shortest_dist, longest_dist = shortest_longest_path_dag(graph, source)

print("Shortest distances from source node:")
for i, dist in enumerate(shortest_dist):
    print(f"Node {i}: {dist}")

print("\nLongest distances from source node:")
for i, dist in enumerate(longest_dist):
    print(f"Node {i}: {dist}")
