import heapq

def prim_mst(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start, None)]  # (cost, current_node, previous_node)
    
    while min_heap:
        cost, current, prev = heapq.heappop(min_heap)
        if current not in visited:
            visited.add(current)
            if prev is not None:
                mst.append((prev, current, cost))
            for neighbor, weight in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor, current))
    
    return mst

def dfs(graph, start, visited, path):
    visited.add(start)
    path.append(start)
    for neighbor, _ in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path)

def tsp_approximation(graph, start):
    mst = prim_mst(graph, start)
    mst_graph = {i: [] for i in graph}
    for u, v, weight in mst:
        mst_graph[u].append((v, weight))
        mst_graph[v].append((u, weight))
    
    visited = set()
    path = []
    dfs(mst_graph, start, visited, path)
    path.append(start)  # Return to the starting city
    
    return path

# Example usage
graph = {
    0: [(1, 2), (2, 9), (3, 10), (4, 7)],
    1: [(0, 2), (2, 6), (3, 4), (4, 3)],
    2: [(0, 9), (1, 6), (3, 8), (4, 5)],
    3: [(0, 10), (1, 4), (2, 8), (4, 1)],
    4: [(0, 7), (1, 3), (2, 5), (3, 1)]
}

start_city = 0
shortest_trip = tsp_approximation(graph, start_city)
print("Approximate shortest trip:", shortest_trip)