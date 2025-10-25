import heapq

def prim(graph, start_node):

    mst = []
    visited = {start_node}
    edges = [(cost, start_node, neighbor) for neighbor, cost in graph[start_node].items()]
    heapq.heapify(edges)

    while edges:
        cost, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, cost))
            for neighbor, cost in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (cost, v, neighbor))
    return mst

if __name__ == "__main__":
    city_graph = {
        'A': {'B': 10, 'C': 15, 'D': 20},
        'B': {'A': 10, 'C': 35, 'D': 25},
        'C': {'A': 15, 'B': 35, 'D': 30},
        'D': {'A': 20, 'B': 25, 'C': 30}
    }

    start_city = 'A'
    minimum_spanning_tree = prim(city_graph, start_city)

    print("Minimum Spanning Tree:")
    for city1, city2, cost in minimum_spanning_tree:
        print(f"{city1} - {city2}: {cost}")