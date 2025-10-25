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
        'Denver': {'Phoenix': 820, 'San Francisco': 1250, 'Los Angeles': 1020, 'San Diego': 1080},
        'Phoenix': {'Denver': 820, 'San Francisco': 750, 'Los Angeles': 370, 'San Diego': 350},
        'San Francisco': {'Denver': 1250, 'Phoenix': 750, 'Los Angeles': 380, 'San Diego': 500},
        'Los Angeles': {'Denver': 1020, 'Phoenix': 370, 'San Francisco': 380, 'San Diego': 120},
        'San Diego': {'Denver': 1080, 'Phoenix': 350, 'San Francisco': 500, 'Los Angeles': 120}
    }

    start_city = 'Denver'
    mst = prim(graph, start_city)
    tour = create_tour(mst, start_city)
    distance = calculate_distance(tour, graph)

    print("Tour:", " -> ".join(tour))
    print("Total Distance:", distance)

if __name__ == "__main__":
    main()
