import math

# Coordinates of the cities (latitude, longitude)
cities = {
    'Denver': (39.74, -104.99),
    'Los Angeles': (34.03, -118.15),
    'San Diego': (32.42, -117.09),
    'Phoenix': (33.26, -112.04),
    'San Fransisco': (37.47, -122.25)
}

def haversine(coord1, coord2):
    # Haversine formula to calculate the distance between two points on the Earth
    R = 6371  # Radius of the Earth in kilometers
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def nearest_neighbor(start, cities):
    unvisited = list(cities.keys())
    unvisited.remove(start)
    path = [start]
    total_distance = 0

    current_city = start
    while unvisited:
        nearest_city = min(unvisited, key=lambda city: haversine(cities[current_city], cities[city]))
        total_distance += haversine(cities[current_city], cities[nearest_city])
        path.append(nearest_city)
        current_city = nearest_city
        unvisited.remove(nearest_city)

    # Return to the starting city
    total_distance += haversine(cities[current_city], cities[start])
    path.append(start)

    return path, total_distance

# Starting city
start_city = 'Denver'
path, total_distance = nearest_neighbor(start_city, cities)

print("Path:", " -> ".join(path))
print(f"Total Distance: {total_distance:.2f} km")
