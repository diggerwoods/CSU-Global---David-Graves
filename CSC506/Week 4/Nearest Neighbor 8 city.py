import numpy as np
import time

# Starts timer for algorithm
start_time = time.time()

# Define the distance matrix for 8 cities
distances = np.array([
    [0, 557, 1726, 611, 830, 1765, 1366, 1631],  # Distances from Denver
    [557, 0, 1242, 1140, 1354, 1247, 857, 1095],  # Distances from Kansas City
    [1726, 1242, 0, 2180, 2338, 1255, 1184, 1097], # Distances from Miami
    [611, 1140, 2180, 0, 271, 2369, 1974, 2233],  # Distances from Las Vegas
    [830, 1354, 2338, 271, 0, 2590, 2193, 2448],  # Distances from Los Angeles
    [1765, 1247, 1255, 2369, 2590, 0, 399, 184], # Distances from Boston
    [1366, 857, 1184, 1974, 2193, 399, 0, 292], # Distances from Buffalo
    [1631, 1095, 1097, 2233, 2448, 184, 292, 0] # Distances from New York
])

def nearest_neighbor_algorithm(start_city, distances):
    num_cities = len(distances)
    visited = [False] * num_cities
    path = [start_city]
    total_distance = 0
    current_city = start_city
    visited[current_city] = True

    for _ in range(num_cities - 1):
        nearest_city = None
        nearest_distance = float('inf')
        for city in range(num_cities):
            if not visited[city] and distances[current_city][city] < nearest_distance:
                nearest_city = city
                nearest_distance = distances[current_city][city]
        path.append(nearest_city)
        total_distance += nearest_distance
        visited[nearest_city] = True
        current_city = nearest_city

    # Return to the starting city
    total_distance += distances[current_city][start_city]
    path.append(start_city)

    return path, total_distance

# Starting from Denver (index 0)
start_city = 0
path, total_distance = nearest_neighbor_algorithm(start_city, distances)

# Print the result
city_names = ['Denver(0)', 'Kansas City(1)', 'Miami(2)', 'Las Vegas(3)', 'Los Angeles(4)', 'New England(5)', 'Buffalo(6)', 'New York(7)']
path_names = [city_names[city] for city in path]
print(f"Path: {' -> '.join(path_names)}")
print(f"Total distance: {total_distance} miles")

# Finds the total time for algorithm and prints
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds")
