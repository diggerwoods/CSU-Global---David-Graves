import numpy as np

# Define the coordinates of the cities
cities = {
    'Denver': (39.7392, -104.9903),
    'Phoenix': (33.4484, -112.0740),
    'San Francisco': (37.7749, -122.4194),
    'Los Angeles': (34.0522, -118.2437),
    'San Diego': (32.7157, -117.1611)
}

# Calculate the distance matrix
def calculate_distance_matrix(cities):
    city_names = list(cities.keys())
    num_cities = len(city_names)
    distance_matrix = np.zeros((num_cities, num_cities))
    
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = geodesic(cities[city_names[i]], cities[city_names[j]]).kilometers
    return distance_matrix, city_names

# Nearest Neighbor Algorithm
def nearest_neighbor_algorithm(distance_matrix, start_index):
    num_cities = len(distance_matrix)
    visited = [False] * num_cities
    path = [start_index]
    visited[start_index] = True
    total_distance = 0
    
    current_city = start_index
    for _ in range(num_cities - 1):
        nearest_city = None
        nearest_distance = float('inf')
        
        for next_city in range(num_cities):
            if not visited[next_city] and distance_matrix[current_city][next_city] < nearest_distance:
                nearest_city = next_city
                nearest_distance = distance_matrix[current_city][next_city]
        
        path.append(nearest_city)
        visited[nearest_city] = True
        total_distance += nearest_distance
        current_city = nearest_city
    
    # Return to the starting city
    total_distance += distance_matrix[current_city][start_index]
    path.append(start_index)
    
    return path, total_distance

# Main function
def main():
    distance_matrix, city_names = calculate_distance_matrix(cities)
    start_city = 'Denver'
    start_index = city_names.index(start_city)
    
    path, total_distance = nearest_neighbor_algorithm(distance_matrix, start_index)
    
    # Print the path and total distance
    print("Optimal Path:")
    for city_index in path:
        print(city_names[city_index], end=" -> ")
    print("\nTotal Distance: {:.2f} km".format(total_distance))

if __name__ == "__main__":
    main()