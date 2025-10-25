import heapq

def dijkstra(graph, start, target):
    # Priority queue to store (distance, node)
    priority_queue = [(0, start)]
    # Dictionary to store the shortest distance to each node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    # Dictionary to store the previous node in the shortest path
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If we reached the target node, we can stop
        if current_node == target:
            break

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstruct the shortest path
    path = []
    while target is not None:
        path.append(target)
        target = previous_nodes[target]
    path.reverse()

    return path, distances[path[-1]]

# Example graph (dictionary of dictionaries)
graph = {
    'Restaurant': {'A': 2, 'B': 5},
    'A': {'Restaurant': 2, 'B': 8, 'C': 7},
    'B': {'Restaurant': 5, 'A': 8, 'C': 2, 'D': 6},
    'C': {'A': 7, 'B': 2, 'D': 3},
    'D': {'B': 6, 'C': 3}
}

# Find the shortest path from 'Restaurant' to 'D'
path, distance = dijkstra(graph, 'Restaurant', 'D')
print(f"Shortest path: {path} with distance {distance}")

#Step-by-Step Guide
#Initialize the Graph:

#Represent the delivery locations and routes as a graph. Each node represents a location (e.g., restaurant, delivery points), and each edge represents the route between locations with a weight (e.g., distance or time).
#Set Up Data Structures:

#Use a priority queue to keep track of the next node to visit based on the shortest known distance.
#Maintain a dictionary to store the shortest distance from the start node to each node.
#Keep a dictionary to store the previous node for each node to reconstruct the path.
#Algorithm Initialization:

#Set the distance to the start node to 0 and all other nodes to infinity.
#Add the start node to the priority queue.
#Algorithm Execution:

#While the priority queue is not empty:
#Extract the node with the smallest distance.
#For each neighboring node, calculate the potential new path distance.
#If the new path distance is shorter, update the shortest distance and the previous node.
#Add the neighboring node to the priority queue if it hasn't been processed.
#Reconstruct the Path:

#Once the algorithm completes, use the previous node dictionary to reconstruct the shortest path from the start node to the target node.