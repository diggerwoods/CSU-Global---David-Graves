import itertools
import time

# Starts timer for algorithm
start_time = time.time()

#Prim's MST Algorithm: This function constructs the MST of the graph.
def prim_mst(graph):
    num_nodes = len(graph)
    selected_nodes = [False] * num_nodes
    selected_nodes[0] = True
    mst_edges = []

    for _ in range(num_nodes - 1):
        min_edge = (None, None, float('inf'))
        for u in range(num_nodes):
            if selected_nodes[u]:
                for v in range(num_nodes):
                    if not selected_nodes[v] and graph[u][v] < min_edge[2]:
                        min_edge = (u, v, graph[u][v])
        mst_edges.append(min_edge)
        selected_nodes[min_edge[1]] = True

    return mst_edges

#DFS Traversal: This function performs a DFS on the MST to generate the TSP path.
def dfs(graph, start):
    visited = [False] * len(graph)
    path = []

    def dfs_util(v):
        visited[v] = True
        path.append(v)
        for u in range(len(graph)):
            if graph[v][u] != 0 and not visited[u]:
                dfs_util(u)

    dfs_util(start)
    return path

#TSP Solution: Combines the MST and DFS to find the TSP path and calculates the total distance traveled.
def tsp_mst_dfs(graph):
    mst_edges = prim_mst(graph)
    mst_graph = [[0] * len(graph) for _ in range(len(graph))]
    for u, v, weight in mst_edges:
        mst_graph[u][v] = weight
        mst_graph[v][u] = weight

    path = dfs(mst_graph, 0)
    path.append(path[0])  # Return to the starting point

    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]

    return path, total_distance

# Define the distance matrix for 12 cities
graph = [
    [0, 557, 1726, 611, 830, 1765, 1366, 1631, 1463, 1020, 878, 998],  # Distances from Denver
    [557, 0, 1242, 1140, 1354, 1247, 857, 1095, 949, 472, 646, 451],  # Distances from Kansas City
    [1726, 1242, 0, 2180, 2338, 1255, 1184, 1097, 328, 817, 967, 1027], # Distances from Miami
    [611, 1140, 2180, 0, 271, 2369, 1974, 2233, 1966, 1576, 1225, 1590],  # Distances from Las Vegas
    [830, 1354, 2338, 271, 0, 2590, 2193, 2448, 2143, 1776, 1370, 1805],  # Distances from Los Angeles
    [1765, 1247, 1255, 2369, 2590, 0, 399, 184, 1017, 941, 1603, 805], # Distances from Boston
    [1366, 857, 1184, 1974, 2193, 399, 0, 292, 880, 626, 1285, 434], # Distances from Buffalo
    [1631, 1095, 1097, 2233, 2448, 184, 292, 0, 835, 758, 1417, 643], # Distances from New York
    [1463, 949, 328, 1966, 2143, 1017, 880, 835, 0, 499, 820, 699],  # Distances from Jacksonville
    [1020, 472, 817, 1576, 1776, 941, 626, 758, 499, 0, 665, 251],  # Distances from Nashville
    [878, 646, 967, 1225, 1370, 1603, 1285, 1417, 820, 665, 0, 865],  # Distances from Houston
    [998, 451, 1027, 1590, 1805, 805, 434, 643, 699, 251, 865, 0]  # Distances from Indianapolis
]

path, distance = tsp_mst_dfs(graph)
print("Path:", path)
print("Total distance traveled:", distance, "miles")

# Finds the total time for algorithm and prints
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds")
