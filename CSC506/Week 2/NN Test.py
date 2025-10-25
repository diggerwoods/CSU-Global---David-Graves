import numpy as np

# Define the cities and their coordinates (latitude, longitude)
cities = {
    'Denver': (39.7392, -104.9903),
    'Los Angeles': (34.0522, -118.2437),
    'Dallas': (32.7767, -96.7970),
    'New York': (40.7128, -74.0060)
}

# Function to calculate the distance between two cities using the Haversine formula
def haversine(coord1, coord2):
    R = 6371  # Radius of the Earth in kilometers
    lat1, lon1 = np.radians(coord1)
    lat2, lon2 = np.radians(coord2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return R * c

# Function to find the nearest neighbor
def nearest_neighbor(start_city, cities):
    unvisited = list(cities.keys())
    unvisited.remove(start_city)
    current_city = start_city
    path = [current_city]
    total_distance = 0

    while unvisited:
        nearest_city = min(unvisited, key=lambda city: haversine(cities[current_city], cities[city]))
        total_distance += haversine(cities[current_city], cities[nearest_city])
        current_city = nearest_city
        path.append(current_city)
        unvisited.remove(current_city)

    # Return to the starting city
    total_distance += haversine(cities[current_city], cities[start_city])
    path.append(start_city)

    return path, total_distance

# Starting city
start_city = 'Denver'

# Find the path and total distance
path, total_distance = nearest_neighbor(start_city, cities)

# Print the results
print("Path:", " -> ".join(path))
print("Total Distance: {:.2f} km".format(total_distance))
