import itertools

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

# Example usage
graph = [
    [0, 557, 611, 830],  # Distances from Denver
    [557, 0, 1140, 1354],  # Distances from Kansas City
    [611, 1140, 0, 271],  # Distances from Las Vegas
    [830, 1354, 271, 0],  # Distances from Los Angeles
]

path, distance = tsp_mst_dfs(graph)
print("Path:", path)
print("Total distance traveled:", distance)


#Prim's MST Algorithm: This function constructs the MST of the graph.
#DFS Traversal: This function performs a DFS on the MST to generate the TSP path.
#TSP Solution: Combines the MST and DFS to find the TSP path and calculates the total distance traveled.