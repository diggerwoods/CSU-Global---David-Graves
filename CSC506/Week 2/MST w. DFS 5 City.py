import heapq

def prim(graph, start):
    mst = []
    visited = set([start])
    edges = [(cost, start, to) for to, cost in graph[start].items()]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))

            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return mst

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

def create_tour(mst, start):
    graph = {}
    for frm, to, cost in mst:
        if frm not in graph:
            graph[frm] = []
        if to not in graph:
            graph[to] = []
        graph[frm].append(to)
        graph[to].append(frm)
    
    tour = dfs(graph, start)
    tour.append(start)  # Return to the starting point
    return tour

def calculate_distance(tour, graph):
    distance = 0
    for i in range(len(tour) - 1):
        distance += graph[tour[i]][tour[i + 1]]
    return distance

def main():
    # Define the graph with distances between cities
    graph = {
        'Denver': {'Phoenix': 1319, 'San Francisco': 2011, 'Los Angeles': 1641, 'San Diego': 1738},
        'Phoenix': {'Denver': 1319, 'San Francisco': 1207, 'Los Angeles': 595, 'San Diego': 563},
        'San Francisco': {'Denver': 2011, 'Phoenix': 1207, 'Los Angeles': 611, 'San Diego': 804},
        'Los Angeles': {'Denver': 1641, 'Phoenix': 595, 'San Francisco': 611, 'San Diego': 193},
        'San Diego': {'Denver': 1738, 'Phoenix': 563, 'San Francisco': 804, 'Los Angeles': 193}
    }

    start_city = 'Denver'
    mst = prim(graph, start_city)
    tour = create_tour(mst, start_city)
    distance = calculate_distance(tour, graph)

    print("Tour:", " -> ".join(tour))
    print("Total Distance:", distance, "km")

if __name__ == "__main__":
    main()
