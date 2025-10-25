import heapq

def prim(graph):
    start_node = list(graph.keys())[0]
    mst = {start_node: {}}
    visited = {start_node}
    edges = [(cost, start_node, neighbor) for neighbor, cost in graph[start_node].items()]
    heapq.heapify(edges)

    while edges:
        cost, node, neighbor = heapq.heappop(edges)
        if neighbor not in visited:
            visited.add(neighbor)
            mst[node][neighbor] = cost
            if neighbor not in mst:
              mst[neighbor] = {}
            mst[neighbor][node] = cost
            
            for next_neighbor, next_cost in graph[neighbor].items():
                if next_neighbor not in visited:
                    heapq.heappush(edges, (next_cost, neighbor, next_neighbor))
    return mst

def dfs(graph, start_node):
    tour = []
    visited = set()

    def dfs_recursive(node):
        visited.add(node)
        tour.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_recursive(neighbor)
    
    dfs_recursive(start_node)
    tour.append(start_node)
    return tour

# City graph representation (adjacency list with edge costs)
city_graph = {
    'Denver': {'Phoenix': 1319, 'San Francisco': 2011, 'Los Angeles': 1641, 'San Diego': 1738},
    'Phoenix': {'Denver': 1319, 'San Francisco': 1207, 'Los Angeles': 595, 'San Diego': 563},
    'San Francisco': {'Denver': 2011, 'Phoenix': 1207, 'Los Angeles': 611, 'San Diego': 804},
    'Los Angeles': {'Denver': 1641, 'Phoenix': 595, 'San Francisco': 611, 'San Diego': 193},
    'San Diego': {'Denver': 1738, 'Phoenix': 563, 'San Francisco': 804, 'Los Angeles': 193}
    }

# Find the Minimum Spanning Tree using Prim's algorithm
mst = prim(city_graph)
print("Minimum Spanning Tree:")
print(mst)

# Create a tour using Depth-First Search
start_city = 'Denver'
tour = dfs(mst, start_city)
print("\nTour using DFS:")
print(tour)